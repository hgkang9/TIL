#### posts(app)->models.py

```python
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

def post_image_path(instance,filename):
    return f'posts/images/{filename}'
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content=models.TextField()
    # image=models.ImageField(blank=True)
    
                
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_posts')
 
#Post: Image = 1:N    
class Image(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    file=ProcessedImageField(
                    upload_to=post_image_path, #저장위치
                    processors=[ResizeToFill(600,600)], #처리할 작업 목록
                    format='JPEG', #저장포멧
                    options={'quality':90}, #옵션
                )
    

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
```



#### posts(app)->forms.py

```python
from django import forms
from .models import Post, Comment, Image

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['content',]
        
        
class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=['file',]
        
        
ImageFormSet= forms.inlineformset_factory(Post, Image, form=ImageForm, extra=3)
        
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'댓글을 작성하세요.'}))
    # content = forms.CharField(label='', widget=forms.Textarea(attrs={'class':'form-control','placeholder':'댓글을 작성하세요.'})) # 조금다름
    
    class Meta:
        model=Comment
        fields=['content',]
```



#### posts(app)->urls.py

```python
from django.urls import path
from . import views

app_name ='posts'

urlpatterns = [
    path('', views.list, name='list'),
    path('explore/', views.explore, name='explore'),
    path('create/',views.create,name='create'),
    path('<int:post_id>/update/',views.update,name='update'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('<int:post_id>/comments/create/',views.comment_create, name='comment_create'),
    path('<int:post_id>/comments/<int:comment_id>/delete/',views.comment_delete, name='comment_delete'),
    path('<int:post_id>/like/',views.like, name='like'),
]
```



#### posts(app)-> views.py

```python
from django.shortcuts import render,redirect,get_object_or_404
from .forms import PostForm, CommentForm, ImageFormSet
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST,require_http_methods
from .models import Post,Comment
from django.db import transaction
from itertools import chain

# Create your views here.

def explore(request):
    posts = Post.objects.order_by('-id').all()
    comment_form= CommentForm()
    return render(request, 'posts/list.html',{'posts':posts, 'comment_form':comment_form})
    

@login_required
def list(request):
    # 1. 내가 follow하고 있는 사람들의 리스트
    followings = request.user.followings.all()
    # 2. followings 변수와 나를 묶음
    followings=chain(followings, [request.user])
    # 3. 이 사람들이 작성한 Post들만 뽑아옴.
    posts = Post.objects.filter(user__in=followings).order_by('-id')
    comment_form= CommentForm()
    return render(request, 'posts/list.html',{'posts':posts, 'comment_form':comment_form})
    
@login_required #로그인이 되었을 때 가능 
def create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST,request.FILES)
        image_formset= ImageFormSet(request.POST, request.FILES)
        if post_form.is_valid()and image_formset.is_valid():
            post=post_form.save(commit=False)
            post.user=request.user
            
            with transaction.atomic():
                # 첫번쨰 
                post.save() #실제 데이터베이스에 저장
                # 두번째
                image_formset.instance = post 
                image_formset.save() # 실제 데이터 베이스에 저장
            
            return redirect('posts:list')
    else:
        post_form=PostForm()
        image_formset = ImageFormSet()
    return render(request, 'posts/form.html',{'post_form':post_form, 'image_formset':image_formset})

@login_required
def update(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    
    if post.user != request.user:
        return redirect('posts:list')
    
    if request.method == 'POST':
        post_form=PostForm(request.POST,instance=post)
        image_formset = ImageFormSet(request.POST, request.FILES, instance=post)
        if post_form.is_valid() and image_formset.is_valid():
            post_form.save()
            image_formset.save()
            return redirect('posts:list')
    else:
        post_form=PostForm(instance=post)
        image_formset = ImageFormSet(instance=post)
    return render(request,'posts/form.html', {'post_form':post_form, 'image_formset':image_formset,})
    
@login_required    
def delete(request, post_id):
    # post= Post.objects.get(pk=post_id)
    post= get_object_or_404(Post, id=post_id)
    
    if post.user != request.user:
        return redirect('posts:list')
    post.delete()
    
    # if post.user == request.user:
    #     post.delete()
    
    return redirect('posts:list')

@login_required  
@require_POST
def comment_create(request,post_id):
    comment_form=CommentForm(request.POST)
    if comment_form.is_valid():
        comment=comment_form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_id
        comment.save()
    return redirect('posts:list')
    
@require_http_methods(['GET','POST'])
def comment_delete(request,post_id,comment_id):
    comment = get_object_or_404(Comment,id=comment_id)
    if comment.user != request.user:
        return redirect('posts:list')
    comment.delete()    
    return redirect('posts:list')

@login_required      
def like(request, post_id):
    post=get_object_or_404(Post, id=post_id)
    
    if request.user in post.like_users.all():
        # 2. 좋아요 취소
        post.like_users.remove(request.user)
    else:
        # 1. 좋아요!
        post.like_users.add(request.user)
   
    return redirect('posts:list')
```



#### posts(app)->templates(html)

```html
<!--list.html-->
{% extends 'base.html' %}
{% block container %}
<h1>Post List</h1>
{%for post in posts %}
{% include 'posts/_post.html' %}
{% endfor %}
{% endblock %}

<!--form.html-->
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block container %}
<h1>Post Form</h1>
<form action="" method="POST" enctype="multipart/form-data">
    {%csrf_token%}
    {%bootstrap_form post_form%}
    {{ image_formset.as_p }} <!--p태그로 감싼다-->
    {% buttons %}
        <button type="submit" class="btn btn-primary">Submit</button>
    {% endbuttons %}
</form>
{% endblock %}

<!--_post.html-->
<div class="card" style="width: 18rem;">
  <div class="card-header">
    {% if post.user.profile.image %}
    <img scr="{{ post.user.profile.image.url }}" width="25" alt="">
    {% endif %}
    <a href="{% url 'people' post.user.username %}">{{ post.user.username }}</a>
  </div>
  
  <div id="post_{{ post.id }}" class="carousel slide" data-ride="carousel">
    <div class="carousel-inner">
      {% for image in post.image_set.all %}
      <div class="carousel-item {% if forloop.counter == 1 %}active{% endif %}">
        <img src="{{ image.file.url }}" class="card-img-top" alt="{{ image.file }}">
      </div>
      {% endfor %}
    <a class="carousel-control-prev" href="#post_{{ post.id }}" role="button" data-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="carousel-control-next" href="#post_{{ post.id }}" role="button" data-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>
  
  <div class="card-body">
    <a href="{% url 'posts:like' post.id %}">
      {% if user in post.like_users.all %}
        <i class="fas fa-heart"></i>
      {% else %}
        <i class="far fa-heart"></i>
      {% endif %}
    </a>
    <p class="card-text">
      {{ post.like_users.count }}명이 좋아합니다.
    </p>

    <p class="card-text">{{ post.content}}</p>
    {% if post.user == user %}
    <a href="{% url 'posts:update' post.id %}" class="btn btn-info">Edit</a>
    <a href="{% url 'posts:delete' post.id %}" class="btn btn-primary">Delete</a>
    {% endif %}
  </div>
  <div class="card-body">
    {% for comment in post.comment_set.all %}
    <div class="card-text">
      <strong>{{comment.user.username}}</strong> {{comment.content}}
      {% if comment.user == user %}
      <a href="{% url 'posts:comment_delete' post.id comment.id %}">삭제</a>
      {% endif %}
    </div>
    {% empty%}
    <div class="card-text">댓글이 없습니다.</div>
    {% endfor %}
  </div>
  {% if user.is_authenticated %}
  <form action="{% url 'posts:comment_create' post.id %}" method="POST">
    {% csrf_token%}
    <div class="input-group">
      {{ comment_form}}
      <div class="input-group-append">
        <input type="submit" value="Submit" class="btn btn-primary"/>
      </div>
    </div>  
  </form>
  {% endif %}
</div>
```


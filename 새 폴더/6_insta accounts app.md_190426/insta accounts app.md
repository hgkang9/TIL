#### insta(project)->urls.py

```python
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
    path('<str:username>/',accounts_views.people, name='people'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```





#### accounts(app)->models.py

```python
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    nickname = models.CharField(max_length=40, blank=True)
    introduction = models.TextField(blank=True)
    image=ProcessedImageField(
                    blank=True,
                    upload_to='profile/image', #저장위치
                    processors=[ResizeToFill(300,300)], #처리할 작업 목록
                    format='JPEG', #저장포멧
                    options={'quality':90}, #옵션
                )
                
class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
```



#### accounts(app)->forms.py

```python
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile 

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model= get_user_model()
        fields = UserCreationForm.Meta.fields
        



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model= get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name',]
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ['nickname', 'introduction', 'image',]
```



#### accounts(app)->views.py

```python
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, ProfileForm, CustomUserCreationForm
from .models import Profile

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list') 
    
    if request.method=='POST':
        signup_form=CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            Profile.objects.create(user=user)  # User의 Profile 생성
            auth_login(request, user)
            return redirect('posts:list')
    else:
        signup_form=CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'signup_form':signup_form})
    
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:list') 
        
    if request.method=='POST':
        login_form=AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect(request.GET.get('next') or 'posts:list')
    else:
        login_form=AuthenticationForm()
    return render(request, 'accounts/login.html', {'login_form':login_form})
    
def logout(request):
    auth_logout(request)
    return redirect('posts:list')
    
def people(request,username):
    #=>get_user_model() #=> User
    people = get_object_or_404(get_user_model(), username=username)
    return render(request, 'accounts/people.html', {'people':people})
    
    
#User Edit(회원정보 수정) - User CRUD 중 U
@login_required
def update(request):
    if request.method == 'POST':
        user_change_form= CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('people', request.user.username)
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/update.html', {'user_change_form':user_change_form})


#User Delete(회원 탈퇴) - User CRUD 중 D    
@login_required
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('posts:list')
    return render(request, 'accounts/delete.html')
    
    
@login_required
def password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)
        if password_change_form.is_valid():
            user=password_change_form.save()
            update_session_auth_hash(request,user)
            return redirect('people', request.user.username)
    else:
        password_change_form = PasswordChangeForm(request.user)
    return render(request,'accounts/password.html', {'password_change_form':password_change_form})
    
def profile_update(request):
    profile=request.user.profile
    if request.method == 'POST':
        profile_form=ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('people', request.user.username)
    else:
        profile_form=ProfileForm(instance=profile)
    return render(request, 'accounts/profile_update.html', {'profile_form':profile_form,})
    
    
def follow(request, user_id):
    people = get_object_or_404(get_user_model(), id= user_id)
    
    if request.user in people.followers.all():
        # 2. people을 unfollow하기
        people.followers.remove(request.user)
    else:
        # 1. people을 follow 하기
        people.followers.add(request.user)
    
    return redirect('people', people.username)
```



#### accounts(app)->urls.py

```python
from django.urls import path
from . import views

app_name='accounts'

urlpatterns=[
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update/',views.update, name='update'),
    path('delete/',views.delete, name='delete'),
    path('password/',views.password, name='password'),
    path('profile/update/',views.profile_update, name='profile_update'),
    path('<int:user_id>/follow/',views.follow, name='follow'),
]
```



#### accounts(app)->templates(html)

```html
<!--signup.html-->
{% extends 'base.html' %}
{% block container %}
<h1>회원 가입</h1>
<form method="POST">
    {% csrf_token %}
    {{ signup_form }}
    <input type="submit" value="Submit"/>
</form>
{% endblock%}

<!--login-->
{% extends 'base.html' %}
{% block container %}
<h1>로그인</h1>
<form method="POST">
    {%csrf_token%}
    {{ login_form }}
    <input type="submit" value="Submit"/>
</form>
{% endblock%}

<!--people.html-->
{% extends 'base.html' %}
{% block container %}
<h1>People</h1>
<div class="container">
    <div class="row">
        <div class="col-3">
            <h1>
                {% if people.profile.image %}
                <img src="{{ people.profile.image.url }}" width="50" alt="{{ people.profile.image}}">
                {% endif %}
                {{ people.username }}
            </h1>
        </div>
        <div class="col-9">
            <div>
                <strong>{{ people.profile.nickname }}</strong>
                {% if user != people %}
                    {% if user in people.followers.all %}
                    <a href="{% url 'accounts:follow' people.id %}">Unfollow</a>
                    {% else %}
                    <a href="{% url 'accounts:follow' people.id %}">follow</a>
                    {% endif %}
                {% endif %}
            </div>
            <div>
                <strong>Followers:</strong>{{ people.followers.count }}
                <strong>Followings:</strong>{{ people.followings.count }}
            </div>
            <div>
                {{ people.profile.introduction }}
            </div>
        </div>
    </div>
    {% if user == people %}
    <div>
        <a href="{% url 'accounts:profile_update' %}">프로필 수정</a>
        <a href="{% url 'accounts:update' %}">계정정보수정</a>
    </div>
    {% endif %}
    <div class="row">
        {% for post in people.post_set.all %}
        <div class="col-4">
            <img src="{{ post.image_set.first.file.url }}" class="img-fluid"/>
        </div>
        {% endfor %}
    </div>
</div>
{% endblock %}

<!--update.html-->
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block container %}
<h1>User Edit</h1>
<form method="POST">
    {% csrf_token %}
    {% bootstrap_form user_change_form %}
    <input type="submit" value="Submit"/>
</form>
<h3>User Delete</h3>
<a href="{% url 'accounts:delete' %}" class="btn btn-danger">회원 탈퇴하기</a>
{% endblock %}

<!--delete.html-->
{% extends 'base.html' %}
{% block container %}
<h1>정말 삭제하시겠습니까?</h1>
<form method="POST">
    {% csrf_token %}
    <p>정말로 탈퇴하시겠습니까?</p>
    <input type="submit" value="탈퇴"/>
</form>
{% endblock%}

<!--password.html-->
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block container %}
<h1>Password Change</h1>
<form method="POST">
    {% csrf_token %}
    {% bootstrap_form password_change_form %}
    <input type="submit" value="Submit"/>
</form>
{% endblock %}

<!--profile_update.html-->
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block container %}
<h1>Profile Edit</h1>
<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {% bootstrap_form profile_form %}
    <input type="submit" value="Submit"/>
</form>
{% endblock%}
```




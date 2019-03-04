from django.shortcuts import render,redirect
from .models import Post,Comment

# Create your views here.
# views.py ->urls.py->templates

def index(request):
    posts = Post.objects.all()
    
    return render(request, 'index.html', {'posts':posts})
    
def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    
    return render(request, 'detail.html', {'post' : post})
 
def delete(request, post_id):
    if request.method == 'POST':
        
        # 삭제하는 코드
        post = Post.objects.get(pk=post_id)
        post.delete()
        return redirect('posts:list')
    else:
        return render(request, 'delete.html')
 
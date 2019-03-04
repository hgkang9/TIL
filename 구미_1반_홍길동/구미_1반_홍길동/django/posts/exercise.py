def index(request):
    posts = Post.objects.all()
    return render(request, 'indext.html', {'posts':posts})

def detail(request, post_id)
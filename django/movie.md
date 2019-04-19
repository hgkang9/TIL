```python
pyenv virtualenv 3.6.7 [가상환경 이름]

pyenv local [가상환경 이름]

pip install django==2.1.8

django-admin startproject [프로젝트 이름] .

./manage.py startapp [앱 이름]

./manage.py runserver $IP:$PORT
```

앱 models.py

```python
from django.db import models

class Genre(models.Model):
    name=models.TextField()
    
class Movie(models.Model):
    title = models.TextField()
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre=models.ForeignKey(Genre, on_delete=models.CASCADE)
    
class Score(models.Model):
    content=models.TextField()
    score=models.IntegerField()
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
```

```
모델 생성 후,
./manage.py makemigrations
./manage.py migrate
```

프로젝트 settings.py

```python
ALLOWED_HOSTS = ['projects-hgkang9.c9users.io']
INSTALLED_APPS에 'movies' 추가
TEMPLATES의 'DIRS'에 os.path.join(BASE_DIR,'project07','templates') 추가
```

프로젝트 urls.py

```python
from django.urls import path, include
urlpatterns에 path('movies/', include('movies.urls')), 추가
```

프로젝트 templates 폴더 생성 -> base.html

```html
body에
{%block container%}    
{%endblock%}
추가
```

앱

```python
urls.py에

from django.urls import path
from . import views

app_name='movies'

urlpatterns = []
```

### list 만들 때

```
templates 생성 -> movies 폴더 생성
```

```python
urls.py에 path('', views.list, name='list'), 추가

views.py에
from django.shortcuts import render, get_object_or_404, redirect
from .models import Genre, Movie, Score

def list(request):
    movies=Movie.objects.all()
    return render(request, 'movies/list.html', {'movies':movies})
```

list.html

```html
{% extends 'base.html' %}
{% block container %}

<h1>Movie List</h1>

{% for movie in movies %}

{% include 'movies/_movie.html' %}

{% endfor %}

{% endblock %}
```

_movie.html

```html
<img src="{{movie.poster_url}}"></img><br>
<a href="{%url 'movies:detail' movie.id%}">{{movie.title}}</a><br>
```

### detail 만들 때

```python
urls.py에 path('<int:movie_id>/', views.detail, name='detail'), 추가

views.py에
from django.shortcuts import render, get_object_or_404, redirect
from .models import Genre, Movie, Score
from .forms import ScoreForm, MovieForm

def detail(request, movie_id):
    movie=get_object_or_404(Movie,id=movie_id)
    score_form=ScoreForm()
    return render(request, 'movies/detail.html', {'movie':movie, 'score_form':score_form })
```

```python
forms.py에
from django import forms
from .models import Score, Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['title','audience','poster_url','description',]
        #fields='__all__' : 모든 요소를 가지고 옴
```

detail.html

```html
{% extends 'base.html' %}
{% block container %}

<h1>영화 정보</h1>

<p>제목 : {{movie.title}}</p>
<p>관객 수 : {{movie.audience}}</p>
<p>영화 포스터 : <img src="{{movie.poster_url}}"></img></p>
<p>세부 정보 : {{movie.description}}</p>
<p>장르 : {{movie.genre.name}}</p>

<h3><a href="{%url 'movies:list'%}">목록으로 돌아가기</a></h3>
{% endblock %}
```

### edit 만들 때

```python
urls.py에 path('<int:movie_id>/edit/', views.edit, name='edit'), 추가

views.py에
from django.shortcuts import render, get_object_or_404, redirect
from .models import Genre, Movie, Score
from .forms import ScoreForm, MovieForm

def edit(request, movie_id):
    movie=get_object_or_404(Movie, id=movie_id)
    if request.method=='POST':
        movie_form=MovieForm(request.POST, instance=movie)
        if movie_form.is_valid():
            movie_form.save()
            return redirect('movies:detail', movie_id)
    else:
        movie_form=MovieForm(instance=movie)
    return render(request, 'movies/edit.html', {'movie_form':movie_form})
```

edit.html

```html
{% extends 'base.html' %}
{% block container %}

<form method="POST">
    {%csrf_token%}
    {{movie_form.as_p}}
    <input type="submit" value="수정"/>
</form>

{% endblock %}
```

```html
detail.html에
<h3><a href="{%url 'movies:edit' movie.id%}">영화 정보 수정</a></h3> 추가
```

### delete 만들 때

```python
urls.py에 path('<int:movie_id>/delete/', views.delete, name='delete'), 추가

views.py에
from django.shortcuts import render, get_object_or_404, redirect
from .models import Genre, Movie, Score
from .forms import ScoreForm, MovieForm

def delete(request, movie_id):
    movie=get_object_or_404(Movie,id=movie_id)
    movie.delete()
    return redirect('movies:list')
```

```html
detail.html에
<h3><a href="{%url 'movies:delete' movie.id%}">영화 정보 삭제</a></h3> 추가
```

### 평점 생성할 때

```python
urls.py에 path('<int:movie_id>/scores/new/', views.score_new, name='score_new'), 추가

views.py에
from django.shortcuts import render, get_object_or_404, redirect
from .models import Genre, Movie, Score
from .forms import ScoreForm, MovieForm
from django.views.decorators.http import require_POST

@require_POST
def score_new(request, movie_id):
    score_form=ScoreForm(request.POST)
    if score_form.is_valid():
        score=score_form.save(commit=False)
        score.movie_id=movie_id
        score.save()
    return redirect('movies:detail', movie_id)
```

```python
forms.py에
from django import forms
from .models import Score, Movie

class ScoreForm(forms.ModelForm):
    content=forms.CharField(label='한줄평', widget=forms.TextInput(attrs={'class':'form_control'}))
    class Meta:
        model=Score
        # fields='__all__'
        fields=['content', 'score',]
```

```html
detail.html에
<h4>한줄평 작성하기</h4>
<form action='{%url "movies:score_new" movie.id%}' method='POST'>
    {%csrf_token%}
    {{score_form.as_p}}
    <input type="submit" value="작성"/>
</form>
추가
```

### 평점 삭제할 때

```python
urls.py에 path('<int:movie_id>/scores/<int:score_id>/delete', views.score_delete, name='score_delete'), 추가

views.py에
from django.shortcuts import render, get_object_or_404, redirect
from .models import Genre, Movie, Score
from .forms import ScoreForm, MovieForm
from django.views.decorators.http import require_POST

@require_POST
def score_delete(request, movie_id, score_id):
    score=get_object_or_404(Score, id=score_id)
    score.delete()
    return redirect('movies:detail', movie_id)
```

```html
detail.html에서 평점 생성 위에
{%for score_comment in movie.score_set.all%}
<p>한줄평 : {{score_comment.content}} // 평점 : {{score_comment.score}}</p>

<form action='{%url "movies:score_delete" movie.id score_comment.id%}' method='POST'>
    {%csrf_token%}
    <input type="submit" value="삭제"/>
</form>
{%endfor%}
추가
```




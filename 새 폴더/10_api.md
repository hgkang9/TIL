# 10_api

urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.genre_list),
    path('genres/<int:genre_id>/', views.genre_detail),
    path('movies/', views.movie_list),
    path('movies/<int:movie_id>/', views.movie_detail),
    path('movies/<int:movie_id>/scores/', views.score_create),
    path('movies/<int:movie_id>/scores/<int:score_id>/', views.score_update_and_delete),
]
```

views.py

```python
from django.shortcuts import render, get_object_or_404
from .models import Genre, Movie, Score
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GenreSerializer, GenreDetailSerializer, MovieSerializer, ScoreSerializer

@api_view(['GET'])
def genre_list(request):
    genres=Genre.objects.all()
    serializer=GenreSerializer(genres, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def genre_detail(request, genre_id):
    genre=get_object_or_404(Genre, id=genre_id)
    serializer=GenreDetailSerializer(genre)
    return Response(serializer.data)
    
@api_view(['GET'])
def movie_list(request):
    movies=Movie.objects.all()
    serializer=MovieSerializer(movies, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def movie_detail(request, movie_id):
    movie=get_object_or_404(Movie, id=movie_id)
    serializer=MovieSerializer(movie)
    return Response(serializer.data)
    
@api_view(['POST'])
def score_create(request, movie_id):
    serializer=ScoreSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id=movie_id)
        return Response({'message':'작성되었습니다.'})
        
@api_view(['PUT', 'DELETE'])
def score_update_and_delete(request, movie_id, score_id):
    score=get_object_or_404(Score, id=score_id)
    if request.method=='PUT':
        serializer=ScoreSerializer(data=request.data, instance=score)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message':'수정되었습니다.'})
    else:
        score.delete()
        return Response({'message':'삭제되었습니다.'})
```

serializers.py

```python
from rest_framework import serializers
from .models import Genre, Movie, Score

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields=['id', 'name',]
        
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=['id', 'title', 'audience', 'poster_url', 'description', 'genre',]
        
class GenreDetailSerializer(serializers.ModelSerializer):
    movie_set=MovieSerializer(many=True)
    class Meta:
        model=Genre
        fields=['id', 'movie_set',]
        
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Score
        fields=['id', 'content', 'score',]
```

models.py

```python
from django.db import models

class Genre(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title=models.CharField(max_length=20)
    audience=models.IntegerField()
    poster_url=models.CharField(max_length=30)
    description=models.TextField()
    genre=models.ForeignKey(Genre, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Score(models.Model):
    content=models.CharField(max_length=30)
    score=models.IntegerField()
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
```

1. 데이터베이스 설계
  db.sqlite3 에서 테이블 간의 관계는 아래와 같습니다.

필드명 자료형 설명
id Interger Primary Key
title String 영화명
audience Integer 누적 관객수
poster_url String 포스터 이미지 URL
description Text 영화 소개
genre_id Integer Genre의 Primary Key(id 값)
Movie

필드명 자료형 설명
id Integer Primary Key
name String 장르 구분
Genre

Score

필드명 자료형 설명
id Integer Primary Key
content String 한줄평(평가 내용)
score Integer 평점
movie_id Integer Movie의 Primary Key(id 값)

2. Seed Data 반영
3. 주어진 movie.json 과 genre.json 을 movies/fixtures/ 디렉토리로 옮깁니다.
4. 아래의 명령어를 통해 반영합니다.

5. admin.py 에 Genre 와 Movie 클래스를 등록한 후, /admin 을 통해 실제로 데이터베이스에 반영
  되었는지 확인해봅시다.
6. movies API
  아래와 같은 API 요청을 보낼 수 있는 서버를 구축해야 합니다.
  허용된 HTTP 요청을 제외하고는 모두 405 Method Not Allowed를 응답합니다.

7. GET /api/v1/genres/

장르의 목록을 요청 받아서 다음과 같은 결과를 응답합니다.
$ python manage.py loaddata genre.json
Installed 11 object(s) from 1 fixture(s)
$ python manage.py loaddata movie.json
Installed 10 object(s) from 1 fixture(s)

curl -X GET "http://localhost:8000/api/v1/genres/" -H "accept:
application/json"

[
{
"id": 1,

2. GET /api/v1/genres/{genre_pk}
  특정 장르의 결과를 응답합니다.
  "name": "가족"
  },
  {
  "id": 2,
  "name": "공포(호러)"
  },
  {
  "id": 3,
  "name": "드라마"
  },
  ...
  ]

{
"id": 3,
"movies": [
{
"id": 2,
"title": "항거:유관순 이야기",
"audience": 1041939,
"poster_url":
"https://ssl.pstatic.net/imgmovie/mdi/mit110/1823/182360_P11_140223.
jpg",
"description": "1919년 3.1 만세운동 후 세평도 안 되는 서대문 감옥 8호실
속, 영혼만은 누구보다 자유로웠던 유관순과 8호실 여성들의 1년의 이야기.",
"genre": 3
},
{
"id": 4,
"title": "증인",
"audience": 2457258,
"poster_url":
"https://ssl.pstatic.net/imgmovie/mdi/mit110/1773/177374_P100_112832
.jpg",
"description": "신념은 잠시 접어두고 현실을 위해 속물이 되기로 마음먹은 민변
출신의 대형 로펌 변호사 ‘순호’(정우성). 파트너 변호사로 승진할 수 있는 큰 기회가 걸린
사건의 변호사로 지목되자 살인 용의자의 무죄를 입증하기 위해 유일한 목격자인 자폐 소녀 ‘지
우’(김향기)를 증인으로 세우려 한다.",
"genre": 3
},
...
],
"name": "드라마"
}

만약, 없는 경로 변수(genre_pk)로 접근하는 경우 404 Not Found 에러를 응답합니다.

3. GET /api/v1/movies
  영화 목록을 요청 받아서 다음과 같은 결과를 응답합니다.

4. GET /api/v1/movies/{movie_pk}
  특정 영화의 결과를 응답합니다.
# 예)
curl -X GET "http://localhost:8000/api/v1/genres/11/" -H "accept:
application/json"
# => 404 Not Found

[
{
"id": 1,
"title": "캡틴 마블",
"audience": 3035808,
"poster_url":
"https://ssl.pstatic.net/imgmovie/mdi/mit110/1326/132623_P22_133853.
jpg",
"description": "1995년, 공군 파일럿 시절의 기억을 잃고 크리족 전사로 살아가던
캐럴 댄버스(브리 라슨)가 지구에 불시착한다. 쉴드 요원 닉 퓨리(사무엘 L. 잭슨)에게 발견
되어 팀을 이룬 그들은 지구로 향하는 더 큰 위협을 감지하고 힘을 합쳐 전쟁을 끝내야 하는
데...",
"genre": 9
},
{
"id": 2,
"title": "항거:유관순 이야기",
"audience": 1041939,
"poster_url":
"https://ssl.pstatic.net/imgmovie/mdi/mit110/1823/182360_P11_140223.
jpg",
"description": "1919년 3.1 만세운동 후 세평도 안 되는 서대문 감옥 8호실 속,
영혼만은 누구보다 자유로웠던 유관순과 8호실 여성들의 1년의 이야기.",
"genre": 3
},
...

만약, 없는 경로 변수(movie_pk)로 접근하는 경우 404 Not Found 에러를 응답합니다.

5. POST /api/v1/movies/{movie_pk}/scores/
  특정 영화에 평점을 등록합니다. 성공시 아래와 같이 응답합니다.

만약, 없는 경로 변수(movie_pk)로 접근하는 경우 404 Not Found 에러를 응답합니다.
필수 필드가 누락된 경우 400 Bad Request 에러를 응답합니다.
6. PUT /api/v1/scores/{score_pk}
  특정 평점을 수정합니다. 성공시 아래와 같이 응답합니다.

만약, 없는 경로 변수(score_pk)로 접근하는 경우 404 Not Found 에러를 응답합니다.
필수 필드가 누락된 경우 400 Bad Request 에러를 응답합니다.
7. DELETE /api/v1/scores/{score_pk}
  특정 평점을 삭제합니다. 성공시 아래와 같이 응답합니다.
  {
  "id": 3,
  "title": "사바하",
  "audience": 2340441,
  "poster_url":
  "https://ssl.pstatic.net/imgmovie/mdi/mit110/1670/167099_P13_101134.
  jpg",
  "description": "사람들은 말했다. 그때, 그냥, 그것이 죽었어야 한다고... 한 시골 마
  을에서 쌍둥이 자매가 태어난다. 온전치 못한 다리로 태어난 ‘금화’(이재인)와 모두가 오래 살
  지 못할 것이라고 했던 언니 ‘그것’. 그것이 태어나고 모든 사건이 시작되었다.",
  "genre": 5
  }

# 예)
curl -X GET "http://localhost:8000/api/v1/movies/1000/" -H "accept:
application/json"
# => 404 Not Found

{
"message": "작성되었습니다."
}

{
"message": "수정되었습니다."
}

{
"message": "삭제되었습니다."
}

만약, 없는 경로 변수(score_pk)로 접근하는 경우 404 Not Found 에러를 응답합니다.

4. API documents
  작성한 API 서버의 가능한 요청 사항과 메서드/경로/경로변수를 테스트 할 수 있는 documents를 구성하여 스크린
  샷을 제출합니다.

-> swagger

pip install django-rest-swagger

settings.py에 app에 rest_framework_swagger 추가

urls.py에 from rest_framework_swagger.views import get_swagger_view

 path('docs/', get_swagger_view(title='API Docs')),

 추가

![캡처](C:\Users\student\Desktop\캡처.JPG)
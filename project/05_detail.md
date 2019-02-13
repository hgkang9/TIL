1. Django Setting
   1. Django 프로젝트를 생성합니다. (이름무관)
   2. detail 이라는 이름의 앱을 생성합니다.
   3. django 설정 중 언어 를 한국어로 설정합니다.
   4. ALLOWED_HOSTS 설정에 "*" 를 추가합니다.

```python
pyenv virtualenv 3.6.7 detail
pyenv local detail
pip install django
django-admin startproject project .
python manage.py startapp detail
python manage.py runserver $IP:$PORT
```

1. base.html 구성
   1. Bootstrap css,js 를 추가하세요
   2. <3.페이지 구성> 에 들어가는 링크들이 모두 들어있는 Nav Bar 를 구성하세요.
        Nav Bar 는 bootstrap navbar component 를 활용해서 구성합니다.
     3. MySite를 클릭하면 / 로 이동합니다.
     4. Q&A를 클릭하면 qna/ 로 이동합니다.
     5. Mypage를 클릭하면 mypage/ 로 이동합니다.
     6. SignUp을 클릭하면 signup/ 으로 이동합니다.
   7. 링크들의 위치는 .d-flex 를 활용하여 아래 예시 이미지와 같이 구성 해주세요.
   8. favicon 을 추가하세요

```html
{%load static%}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.0/css/bootstrap.min.css" integrity="sha384-PDle/QlgIONtM1aqA2Qemk5gPOE7wFq8+Em+G/hmo5Iq0CCmYZLv3fVRDJ4MMwEA" crossorigin="anonymous">
    <link rel="stylesheet" href="{% static 'base.css' %}"/>
    <link href="https://fonts.googleapis.com/css?family=Gamja+Flower" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=East+Sea+Dokdo|Gamja+Flower" rel="stylesheet">
    <link rel="icon" type="image/png" sizes="96x96" href="{% static 'mario.png' %}">
    <title>Document</title>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="/">My Site</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
            aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav w-100">
                <li class="nav-item active d-flex align-items-start">
                    <a class="nav-link" href="/qna">Q&A <span class="sr-only">(current)</span></a>
                </li>
                <div class="w-100 d-flex justify-content-end">
                    <li class="nav-item">
                        <a class="nav-link" href="/mypage">Mypage</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/signup">Signup</a>
                    </li>
                </div>
            </ul>
        </div>
    </nav>
    {% block container %}
    
    
    {% endblock %}
    
    
    
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.0/js/bootstrap.min.js" integrity="sha384-7aThvCh9TypR7fIc2HV4O/nFMVCBwyIUKL8XCtKE+8xgCgl/PQGuFsvShjr74PBp" crossorigin="anonymous"></script>
</body>
</html>
```

1. 페이지 구성

   <3.페이지 구성> 에서 사용하는 html 파일들은 base.html 을 extends 시켜서 만들어주세요.

   1. `/`
        시맨틱 태그 header 와 footer 를 사용하여 페이지를 구성합니다.
          960px 보다 작은 화면은 고려하지 않아도 됩니다.
   2. Header
        Navigation Bar 바로 아래에 위치합니다.
          높이는 350px , 너비는 브라우저 전체 영역입니다.
          이미지는 선택적으로 활용 가능하되 반드시 배경 이미지가 있어야 합니다.
          Header 영역의 수직/수평 가운데 정렬 위치 에 h1 태그를 사용하여 작성 해주세요.
   3. Footer
        브라우저 최하단에 위치합니다.
          높이는 50px 이상, 너비는 브라우저 전체 영역입니다.
          왼쪽에는 본인의 이름 혹은 닉네임, 오른쪽에는 헤더로 올라가는 링크로 구성됩니다.
          bootstrap Utilities의 Spacing 을 활용하여 좌우 padding 을 만들어줍니다.
          예시이미지

   ```css
   header{
       background-image:url(im.jpg);
       background-position: center center;
       height:350px;
       width:100%;
       background-size: cover;
       font-family: 'Gamja Flower', cursive;
   }
   
   footer{
       background-color: ivory;
       position: fixed;
       height:50px;
       width:100%;
       font-family: 'East Sea Dokdo', cursive;
   }
   
   ```

   ```html
   {% extends 'base.html' %}
   
   {% block container %}
   
       <header class="d-flex justify-content-center align-items-center" id="header">
           <h1 class="text-center">
               Header
           </h1>
       </header>
   
   
       <footer class="fixed-bottom d-flex justify-content-between align-items-center px-5">
           <span>SSAFY</span>
           <a href="#header" class="top">상단으로 올라가기</a>
       </footer>
   
   {% endblock %}
   ```

   1. `signup/`
        회원가입페이지
          960px 보다 작은 화면은 고려하지 않아도 됩니다.
          Bootstrap Form`을 사용합니다.
          이메일, 이름, 비밀번호, 비밀번호 확인 을 위한 input tag를 사용합니다.
          Bootstrap Grid System 을 사용하여 화면 좌측엔 이미지, 우측엔 데이터를 입력할 폼을
          보여줍니다.
          예시 이미지

   ```html
   {% extends 'base.html' %}
   {% load static %}
   {% block container %}
   
       <div class="container">
           <div class="row">
               <div class="col">
                   <img src="{% static 'lion.png' %}" class="w-100"></img>
               </div>
               <div class="col">
                   <h1 class="text-center">Sing Up</h1>
                   <form>
                       <div class="form-group">
                           <label for="exampleInputEmail1">Email address</label>
                           <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
                       </div>
                       <div class="form-group">
                           <label for="exampleInputEmail1">Name</label>
                           <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
                       </div>
                       <div class="form-group">
                           <label for="exampleInputPassword1">Password</label>
                           <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
                       </div>
                       <div class="form-group">
                           <label for="exampleInputPassword1">Password Confirm</label>
                           <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
                       </div>
                       <button type="submit" class="btn btn-primary">Submit</button>
                   </form>
               </div>
           </div>
       
   
   
   
   {% endblock %}
   ```

   1. mypage/
        유저 정보를 출력하는 페이지
          사용자의 개인정보와 작성 글을 보여줄 페이지입니다.
          960px 보다 작은 화면은 고려하지 않아도 됩니다.
          화면 좌측엔 사용자의 정보, 우측엔 사용자가 작성한 글 목록을 보여줍니다.
          좌측의 사용자 정보는 Bootstrap Card 를 활용해서 구성합니다.
          사용자의 이미지는 .rounded-circle 를 사용하여 원형으로 표시합니다.
          이미지는 장고 프로젝트 내부의 이미지를 스태틱으로 적용시킵니다.
          사용자의 정보를 보여주는 Card는 .position-fixed 를 사용하여 스크롤을 아래로
          내리더라도 좌측에 그대로 유지 시켜서 사용자에게 보여줍니다.

   ```html
   {% extends 'base.html' %}
   {% load static %}
   {% block container %}
   
       <div class="container">
           <div class="row">
               <div class="col">
                   <div class="card position-fixed" style="width: 20rem;">
                       <img src="{% static 'qsqs.jpg' %}" class="card-img-top rounded-circle" alt="...">
                       <div class="card-body">
                           <h5 class="card-title">Name</h5>
                           <h6 class="card-subtitle mb-2 text-muted">name@ssafy.com</h6>
                           <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                           <a href="#" class="btn btn-primary">Logout</a>
                       </div>
                   </div>
               </div>
               <div class="col">
                   <div class="card mb-3">
                       <img src="{% static 'cat.jpg' %}" class="card-img-top" alt="...">
                       <div class="card-body">
                           <h5 class="card-title">작성글</h5>
                           <p class="card-text">hi</p>
                           <a href="#" class="btn btn-primary">Go somewhere</a>
                       </div>
                   </div>
               </div>
           </div>
       
   {% endblock %}
   ```

   1. qna/
        사용자의 질문을 받기 위한 페이지 입니다.
          Bootstrap Form 을 사용합니다.
          제목, 이메일, 내용 을 위한 input tag를 사용합니다.
          960px 보다 큰 화면 에서는 다음과 같이 화면을 구성합니다960px 보다 작은 화면 에서는 다음과 같이 화면을 구성합니다.

   ```html
   {% extends 'base.html' %}
   {% load static %}
   {% block container %}
   
       <div class="container">
           <form>
               <h1 class="text-center">Q & A</h1>
               <div class="form-row">
                   <div class="form-group col-12 col-lg-6">
                       <label for="inputTitle">제목</label>
                       <input type="text" class="form-control" id="inputTitle" placeholder="">
                   </div>
                   <div class="form-group col-12 col-lg-6">
                       <label for="inputEmail4">이메일</label>
                       <input type="email" class="form-control" id="inputEmail4" placeholder="">
                   </div>
               </div>
               <div class="form-group">
                   <label for="exampleFormControlTextarea1">내용</label>
                   <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
               </div>
               <button type="submit" class="btn btn-primary">Submit</button>
           </form>
       </div>    
   {% endblock %}
   ```

   1. ` <str:not_found>/`
        위에서 만든 경로를 제외한 다른 요청이 들어오면 보여줄 404페이지
          960px 보다 작은 화면은 고려하지 않아도 됩니다.
          variable routing 을 활용하여 사용자가 잘못 입력한 경로를 잘못된 경로라고 표시해줍니다.

   ```html
   {% extends 'base.html' %}
   {% block container %}
   
       <h1 class="d-flex justify-content-center align-items-center">
           {{ not_found }}는 없는 경로입니다.
       </h1>
       
   {% endblock %}
   ```
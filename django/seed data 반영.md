# seed data 반영

python manage.py loaddata genre.json

python manage.py loaddata movie.json

/admin을 통해 실제 DB에 반영되었는지 확인

1. 영화 생성을 위한 사용자 Form
   1. (필수) 영화목록 에서 a 태그 혹은 버튼을 만듭니다. (Form을 요청하는 URL은 GET
     /movies/new 입니다.)
   2. (필수) 템플릿 파일 이름은 form.html 으로 영화 수정 페이지와 같이 공유합니다.
   3. (필수) id 를 제외한 모든 필드에 맞는 form 과 input 을 제공합니다.
   4. (선택) poster_url 필드 대신 poster_image를 통해 미디어 파일 업로드 기능을 이용하여도 됩니
     다.

2. 영화 생성

  1. (필수) 해당 요청을 처리하는 URL은 POST /movies/new 입니다.
  2. (필수) 검증을 통해 유효한 경우 데이터베이스에 저장을 하며, 아닌 경우 오류 메시지와 함께
    form.html 을 반환합니다.
  3. (필수) 데이터베이스에 저장되면, 영화 정보 조회 GET /movies/<int:movie_pk> 로
    redirect 합니다.

3. 영화 수정을 위한 사용자 Form
   1. (필수) 영화 정보 조회 페이지에서 a 태그 혹은 버튼을 만듭니다. (Form을 요청하는 URL은 GET
     /movies/<int:movie_pk>/edit 입니다.)
   2. (필수) 템플릿 파일 이름은 form.html 으로 영화 생성 페이지와 같이 공유합니다.
   3. (필수) id 를 제외한 모든 필드에 맞는 form 과 input 을 제공합니다.
   4. (선택) poster_url 필드 대신 poster_image를 통해 미디어 파일 업로드 기능을 이용하여도 됩니
     다.

4. 영화 수정
   1. (필수) 해당 요청을 처리하는 URL은 POST /movies/<int:movie_pk>/edit 입니다.
   2. (필수) 검증을 통해 유효한 경우 데이터베이스에 변경내용을 저장 하며, 아닌 경우 오류 메시지와 함
     께 form.html 을 반환합니다.
   3. (필수) 데이터베이스에 수정되면, 영화 정보 조회 GET /movies/<int:movie_pk> 로
     redirect 합니다.





   1. (선택) 평점 생성
   2. 영화 정보 조회 페이지에서 form 을 통해 평점을 작성할 수 있습니다.
   3. 평점 생성 URL은 POST /movies/1/scores/new , POST /movies/2/scores/new 등 이
     며, 동적으로 할당되는 부분이 존재합니다. 동적으로 할당되는 부분에는 데이터베이스에 저장된 영
     화 정보의 Primary Key가 들어갑니다.
   4. 검증을 통해 유효한 경우 데이터베이스에 저장을 하며, 아닌 경우 영화 정보 조회 페이지 로
     Redirect 합니다.
   5. 데이터베이스에 저장되면, 해당하는 영화의 영화 정보 조회 페이지로 Redirect 합니다.
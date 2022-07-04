# drf_project

#예시
python manage.py makemigration
python manage.py migrate
를 통한 데이터베이스 생성 및 반영

$ python manage.py createsuperuser 을 통해 관리자 계정 생성 
리뷰 작성 시 httpie 라이브러리를 통해 명령어 커맨드라인으로 추가 및 업데이트 
# http --auth admin:@@@@@@@ POST http://localhost:8000/post/ content="첫번째 테스트 "
# http --auth admin2:@@@@ PATCH http://localhost:8000/post/1/ content="첫번째 테스트 업데이트 테스트2"

또는

http://127.0.0.1:8000/post를 통해 들어가서 전체 데이터 확인 및 생성 및 업데이트 
우측 User_select / Public 쿼리를 통해 들어가 각각의 테스트 쿼리문 확인 가능 

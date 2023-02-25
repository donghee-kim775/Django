# Django

## Anaconda
> 환경구축

## 1. 환경 생성

~~~
conda create -n django_env python=3.6 django
~~~

---
## 2. 프로젝트 생성

~~~
(django_env) C:~~\Project> mkdir
(django_env) C:~~\Project> cd mysite
(django_env) C:~~\Project\mysite> django-admin startprojectt config .
~~~


장고 프로젝트 내용물 확인
---
C:~~\Project\mysite
- config\
  - asgi.py
  - settings.py
  - urls.py
  - wsgi.py
  - __init__.py  
- manage.py

---
## 3. 개발 서버 구동

~~~
(django_env) C:~~\Project\mysite> python manage.py runserver
~~~

---
## 4. settings.py 파일 수정하기

~~~
(...생략...)
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
(...생략...)
~~~
언어와 시간을 한국 값으로 바꾸어진다.

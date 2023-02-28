# 개요

장고는 모델(Model)을 이용하여 데이터를 관리한다.

보통 데이터 베이스에 데이터를 저장하고 조회하기 위해서 SQL 쿼리문을 이용해야하지만 장고의 모델(Model)을 사용하면 이런 SQL 쿼리문의 도움없이 데이터를 쉽게 처리할 수 있다.

---

## 장고 앱 migrate

모델을 알아보기 위해 python manage.py runserver 명령 실행시 나오는 경고 메시지를 더 자세히 살표보자

~~~
(django_env) c:\projects\mysite>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

__You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.__
__Run 'python manage.py migrate' to apply them.__
......
~~~

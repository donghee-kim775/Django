# 개요

장고는 모델(Model)을 이용하여 데이터를 관리한다.

보통 데이터 베이스에 데이터를 저장하고 조회하기 위해서 SQL 쿼리문을 이용해야하지만 장고의 모델(Model)을 사용하면 이런 SQL 쿼리문의 도움없이 데이터를 쉽게 처리할 수 있다.

---

# 장고 앱 migrate

모델을 알아보기 위해 python manage.py runserver 명령 실행시 나오는 경고 메시지를 더 자세히 살펴보자.

---

## 1. 장고 개발 서버 구동시 나오는 경고 메세지 살펴보기

~~~
(django_env) c:\projects\mysite>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
......
~~~

>중간에 __You have 18 unapplied migration(s).('아직 적용되지 않은 18개의 migration이 있다')__ 고 한다.

->migration이 무엇인지 아직 정확히는 모른다. 하지만 이 경고 메세지는 admin, auth, contenttypes, sessions앱과 관련된 내용이다.

> __Run 'python manage.py migrate' to apply them.__

-> 이 오류를 해결하려면 python manage.py migrate를 실행해야 한다는 안내는 확인할 수 있다.


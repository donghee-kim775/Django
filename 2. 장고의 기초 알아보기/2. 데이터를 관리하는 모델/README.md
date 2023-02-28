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

-> migration이 무엇인지 아직 정확히는 모른다. 하지만 이 경고 메세지는 admin, auth, contenttypes, sessions앱과 관련된 내용이다.

-> __migrations란?__ 모델의 변경 내역을 DB * 스키마에 적용시키는 장고의 방법

> __Run 'python manage.py migrate' to apply them.__

-> 이 오류를 해결하려면 python manage.py migrate를 실행해야 한다는 안내는 확인할 수 있다.

---

## 2. config/settings.py 열어 기본으로 설치된 앱 확인하기

그러면 경고 메세지에 표시된 앱은 어디서 확인할 수 있고, 왜 경고 메시지에 언급되었을까?

그 이유는 config/settings.py 파일을 열어 보면 어느 정도 짐작할 수 있다. 파일을 열어 __INSTEAD_APPS__ 항목을 찾아보자
~~~python
(...생략...)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
(...생략...)
~~~

INSTEAD_APPS는 현재 장고 프로젝트에 설치된 앱이다.

경고 메시지에 언급되지 않은 messages, staticfiles 앱도 보일 것이다. 이 앱들은 데이터베이스와 상관 없으므로 경고 메시지에 언급되지 않은 것이다.

> 데이터 베이스가 필요한 앱만 migrate가 필요하다.

---

## 3. config/settings.py에서 데이터 베이스 정보 살펴보기

config/settings.py 파일을 잘 살펴보면 데이터베이스에 대한 정보도 정의되어 있다.

~~~python
(... 생략 ...)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
(... 생략 ...)
~~~

DATABASES 설정 중 default의 'ENGINE' 항목을 보면 데이터베이스 엔진이 django.db.backends.sqlite3로 정의 되어있다.

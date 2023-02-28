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

-> 이 오류를 해결하려면 __python manage.py migrate__ 를 실행해야 한다는 안내는 확인할 수 있다.

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

DATABASES 설정 중 default의 __'ENGINE'__ 항목을 보면 데이터베이스 엔진이 __django.db.backends.sqlite3__ 로 정의 되어있다.

그리고  __'NAME'__ 항목을 보면 데이터베이스는 __BASE_DIR__ 에 있는 __db.sqlite3__ 파일에 저장되는 것도 알 수 있다.

> SQLite는 소규모 프로젝트에서 사용되는 가벼운 데이터 베이스이다. 서비스로 제공할 때 운영 환경에 어울리는 데이터베이스로 바꾼다.

---

## 4. migrate 명령으로 앱이 필요로 하는 테이블 생성하기

이제 경고 문구에서 안내하는 것처럼 __python manage.py migrate__ 명령을 실행하여 해당 앱들이 필요로 하는 데이터베이스 테이블들을 생성해보자.

~~~
(mysite) c:\projects\mysite>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
~~~

migrate를 수행하면 admin, auth, concenttypes, sessions 앱들이 사용하는 테이블들이 생성된다.

어떤 테이블들이 생성되는지 알 필요는 없다. 위의 앱들을 사용하더라도 테이블을 직접 건드릴 일은 없기 때문이다.

장고의 장점 중 하나는 테이블 작업을 위해 직접 쿼리문을 수행하지 않아도 된다는 점이다.

장고의 ORM(Object Relational Mapping)을 사용하면 쿼리문을 몰라도 작업을 쉽게 할 수 있다.

> __ORM이란?__ 파이썬으로도 데이터 작업을 할 수 있게 해주는 기능 / 즉, 장고에서는 쿼리문을 몰라도 파이썬을 안다면 데이터를 다룰 수 있다.

---

## 5. 모델 만들기

이제 pybo가 사용할 데이터 모델을 만들어 보자.
> pybo에는 __질문과 답변__ 에 해당하는 데이터 모델이 있어야한다.

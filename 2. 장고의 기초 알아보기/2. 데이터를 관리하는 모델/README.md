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

### 질문 모델
- subject : 질문의 제목
- content : 질문의 내용
- create_date : 질문을 작성한 일시

### 답변 모델
- question : 질문 (어떤 질문의 답변인지 알아야 하므로 질문 속성이 필요함)
- content : 답변의 내용
- create_date : 답변을 작성한 일시

### pybo/models.py에 질문/ 답변 모델 작성하기

~~~python
from django.db import models

# Question Model
class Question(models.Model):
    # 질문의 제목
    subject = models.CharField(max_length=200)
    # 질문의 내용
    content = models.TextField()
    # 작성일시
    create_date = models.DateTimeField()

# Answer Model
class Answer(models.Model):
    # 질문
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 답변의 내용
    content = models.TextField()
    # 답변을 작성한 일시
    create_date = models.DateTimeField()
~~~

### Question Model
- subject(질문의 제목)
    - CharField : 제목처럼 글자수의 길이가 제한된 텍스트
    
- content(질문의 내용)
    - TextField : 내용처럼 글자수의 길이가 제한되지 않은 텍스트
    
- create_date(답변을 작성한 일시)

### Answer Model
Answer Model은어떤 질문에 대한 답변이므로 Question 모델을 속성으로 가져야 한다.

- question(질문)
이처럼 어떤 모델이 다른 모델을 속성으로 가지면 ForeignKey를 이용한다.
- ForeignKey : 다른 모델과 연결하기 위해 사용
    - on_delete=models.CASCADE : 이 답변과 연결된 질문(Question)이 삭제될 경우 답변(Answer)도 삭제된다. (질문 하나에는 무수히 많은 답변이 등록될 수 있기에)
    
- content(답변의 내용)
    - TextField : 내용처럼 글자수의 길이가 제한되지 않은 텍스트
    
- create_date(답변을 작성한 일시)

> 장고에서 사용하는 속성(Field)의 타입은 이것 외에도 많다. 다음 URL에서 어떤 것들이 있는지 참고하도록 하자.
URL : https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types

---
## 6. 테이블 생성하기

이전 단계에서 만든 모델을 이요하여 테이블을 생성하자.

테이블 생성을 위해 가장 먼저 해야하는 일은 INSTALLED_APPS 항목에 pybo앱을 추가하는 일이다.

### config/settings.py를 열어 pybo 앱 등록하기

~~~python
(... 생략 ...)
INSTALLED_APPS = [
    'pybo.apps.PyboConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    (... 생략 ...)
]
(... 생략 ...)
~~~

INSTALLED_APPS에 추가한 pybo.apps.PyboConfig 클래스는 pybo/apps.py파일에 있는 클래스이다.

### pybo/apps.py 살피기

~~~python
from django.apps import AppConfig

class PyboConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pybo'
~~~

> 이 파일에 정의된 PyboConfig클래스가 config/settings.py파일의 INSTEAD_APPS항목에 추가되지 않으면 장고는 pybo앱을 인식하지 못하고 데이터베이스 관련 작업도 할 수 없다는 사실이다.

> 모델은 앱에 종속되어 있으므로 반드시 장고에 앱을 등록해야 테이블작업을 진행할 수 있다.

### migrate로 테이블 생성하기

우선 __python manage.py migrate__ 를 실행하려면?

__모델이 새로 생성되거나 변경된 경우__ migrate 명령을 실행하려면 작업 파일이 필요하다.

-> 테이블 작업을 만드는 명령어 : __python magage.py makemigrations__

~~~
(djang_env) c:\projects\mysite> python manage.py makemigrations
Migrations for 'pybo':
  pybo\migrations\0001_initial.py
    - Create model Question
    - Create model Answer
~~~

- makemigrations : 장고가 테이블 작업을 수행하기위한 파일들을 생성
- migrate : 실제 테이블 생성

makemigrations를 수행하게되면

- mysite
    - config
    - pybo
        - __migrations__
            - __init__
            - __0001_initial.py__

라는 파일이 생긴다.

makemigrations명령을 한번 더 실행해도 'No changes detected'라는 메시지가 뜬다.

-> '모델 변경사항 없음'을 뜻함(모델 변경사항이 없다면)

이후, python manage.py migrate를 실행하게 되면

~~~
(django_env) c:\projects\mysite> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, pybo, sessions
Running migrations:
  Applying pybo.0001_initial... OK

(django_env) c:\projects\mysite>
~~~

이후 SQL을 보게되면 테이블이 생성되었는 것을 확인할 수 있다.

Question 모델 : pybo_question

Answer 모델 : pybo_answer

-> 위와 같이 생성된 것을 볼 수 있다.

---

## 데이터 저장 / 조회 / 수정 / 삭제

### 1. 장고셸 실행하기(모델 사용하기)

~~~
(django_env) c:\projects\mysite> python manage.py shell
Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
~~~
__python manage.py shell__

일반적인 파이썬 셸을 실행하는 것이 아니라, 장고에 필요한 환경들이 자동으로 설정된 장고 셸이 실행된다.

### 2. Questions 모델로 Questions 모델 데이터 만들기

#### Question과 Answer 모델은 장고 셸에서 다음처럼 import하여 사용하기

~~~
>>> from pybo.models import Question, Answer
~~~

#### Question 모델을 이용하여 질문 데이터를 만들어 보자.

~~~
>>> from django.utils import timezone
>>> q = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다.', create_date=timezone.now())
>>> q.save()
~~~

Question 모델의 subject 속성 : 제목 입력

Question 모델의 content 속성 : 문자열로 질문 내용 입력

Question 모델의 create_date 속성 : DateTimeField 타입이므로 timezone.now()로 현재일시 대입한다.

위처럼 Question모델의 객체 q를 생성한 후 save함수를 실행하면 질문 데이터가 1건 생성된다.

~~~
>>q.id
1
~~~

> id : 모델 데이터의 유일한 값, 프라이머리 키(PK : Primary Key)

데이터가 1건 생성되면 반드시 다음처럼 id값이 생성된다.

이 id 값은 데이터를 생성할때마다 1씩 증가된다.

그러면 두번째 질문을 만들어보자.

~~~
>>> q = Question(subject='장고 모델 질문입니다.', content='id는 자동으로 생성되나요?', create_date=timezone.now())
>>> q.save()
>>> q.id
2
~~~

두번째로 생성한 질문의 id는 예상대로 2라는 것을 알 수 있다.

---

### 3. 데이터 조회

이번에는 저장한 데이터를 조회 해보자.

~~~
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>, <Question: Question object (2)>]>
~~~
__Question.objects.all()__ : 모든 Question 데이터를 조회하는 함수

Question모델의 데이터는 __Question.objects.all()__ 을 통해서 조회할 수 있다.

결과 값 : QuerySet객체가 리턴되는데 위처럼 Question 객체를 포함

Question object(1) : 1은 Question 데이터의 id값

Question object(2) : 2는 Question 데이터의 id값

#### 모델 데이터 조회 결과에 속성값 보여주기

projects/mysite/pybo/models.py

~~~python
(... 생략 ...)

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

# 수정 사항
    def __str__(self):
        return self.subject

(... 생략 ...)
~~~

이렇게 수정하고 Question.objects.all() 함수를 다시 실행하기전,

> 모델이 변경되었으므로 장고 셸을 재시작해야한다.

> 장고 셸을 종료하는 방법은 quit() 혹은 Ctrl+z 입력하면 된다.

~~~
(django_env) c:\projects\mysite>python manage.py shell
>>> from pybo.models import Question, Answer
>>> Question.objects.all()
<QuerySet [<Question: pybo가 무엇인가요?>, <Question: 장고 모델 질문입니다.>]>
>>>
~~~

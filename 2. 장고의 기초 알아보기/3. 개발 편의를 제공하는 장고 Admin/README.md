# 개요

장고(Django)가 기본적으로 제공하는관리자 페이제에 로그인하기 위해서는 superuser를 만들 필요가 있다.

---
## 슈퍼 유저 생성하기

슈퍼 유저 생성 : python manage.py createsuperuser

~~~
(django_env) c:\projects\mysite> python manage.py createsuperuser
사용자 이름 (leave blank to use 'pahke'): admin
이메일 주소: admin@mysite.com
Password:
Password (again):
비밀번호가 너무 짧습니다. 최소 8 문자를 포함해야 합니다.
비밀번호가 너무 일상적인 단어입니다.
비밀번호가 전부 숫자로 되어 있습니다.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

(django_env) c:\projects\mysite>
~~~

위 코드는 다음과 같은 정보로 슈퍼유저를 생성했다.

- 사용자 이름 : admin
- 이메일 주소 : admin@mysite.com
- Password : 1111

> 패스워드는 Anaconda Prompt에서 입력해도 표기가 되지않는다.

> 실제 운영환경에서는 이렇게 보안에 취약한 비밀번호를 사용하면 안된다.

---
## 장고 관리자 화면

슈퍼유저가 생성되었으니 로컬 서버를 구동한 후 http://localhost:8000/admin/ 페이지에 접속해보자

접속 방법
~~~
(django_env) c:\projects\mysite> python manage.py runserver
~~~

![image](https://user-images.githubusercontent.com/54052704/222899868-f6c35233-4da1-4fd4-872f-cb9a3eb4ed13.png)

이러한 화면이 뜰 것이다.

그리고 위와 같이 사용자 이름과 PassWord를 입력하면

![image](https://user-images.githubusercontent.com/54052704/222899952-888fa395-2106-43ea-8d90-51a2f642d141.png)

위와 같은 이미지가 뜬다.

---
## 모델관리

우리는 Question, Answer 모델을 만들었다. 이 모델들을 장고 Admin에 등록하면 손쉽게 모델을 관리할 수 있다.

-> 이말은 쉽게 말해 장고셸로 수행했던 데이터 저장, 수정, 삭제 등의 작업을 장고 Admin에서 할 수 있다.

[파일 : C:/projects/mysite/pybo/admin.py]
~~~python
from djnago.contrib import admin
from .models import Question

admin.site.register(Question) #추가 사항
~~~

위 코드를 입력하게되면 Question 모델을 장고 Admin에 등록하는 것이 된다.

이후 새로고침을 하게 되면

![image](https://user-images.githubusercontent.com/54052704/222960584-c69db229-e05f-49b0-8b88-98ba9884efce.png)

---
## Question 모델 데이터 추가하기

화면에서 Question 모델의 <+추가> 버튼을 누르면 Question 모델의 데이터 등록화면이 나타난다.

이어서 Question 모델의 속성에 맞는 값을 입력하고 <저장> 버튼을 누르면 Question 모델 데이터가 추가된다.

![image](https://user-images.githubusercontent.com/54052704/222960762-05867264-cac5-409a-8e71-e3a588ebdcc8.png)

---
## 장고 Admin에 데이터 검색 기능 추가하기

장고 Admin에서 __제목__ 으로 __질문__ 을 검색할 수 있도록 항목을 추가하자.

pybo/admin.py 파일에 QuestionAdmin 클래스를 추가하고 __search_fields__ 에 __'subject'__ 를 추가하자.

[파일 : C:/projects/mysite/pybo/admin.py]
~~~python
from django.contrib import admin
from .models import Question

# 추가 사항
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

# 변경 사항
admin.site.register(Question, QuestionAdmin)
~~~

새로고침을 하면 밑과 같은 화면이 나타난다.

![image](https://user-images.githubusercontent.com/54052704/222961143-33fd3241-cc37-4c8a-83c7-011d7553c1af.png)

 검색어로 '장고'로 입력하고 <검색>을 눌러보면 제목에 '장고'가 포함된 Question 모델 데이터만 조회된다.

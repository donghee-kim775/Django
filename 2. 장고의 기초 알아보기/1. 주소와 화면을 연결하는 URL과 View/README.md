# 개요

1장에서는 mysite프로젝트를 생성했다. 프로젝트에는 장고가 제공하는 기본 앱과 개발자가 직접 만든 앱이 포함될 수 있다.
장고에서 말하는 '앱'은 안드로이드 앱과 성격이 다르다
장고의 앱이란 무엇일까? 우리의 파이보 서비스에 필요한 pybo앱을 만들어보며 알아보자.

---

## pybo 앱 생성하기

~~~
(django_env) C:~~\Project\mysite> django-admin startapp pybo
~~~

### pybo 앱 구성

C:~~\Project\mysite\pybo
- migrations\
  - __init__.py  
- __intit__.py
- admin.py
- apps
- models
- tests
- views

---

아마 1장에서 봤던 개발 서버를 구동하게 되면 'Page not found(404)'라는 오류 페이지가 보일 것이다. 이 오류는 HTTP 오류코드 중 하나로 사용자가 요청한 페이지를 찾을 수 없는 경우 발생하는 오류이다.

이 오류는 왜 발생했을까?

장고는 사용자가 웹 브라우저에서 /pybo/라는 페이지를 요청하면 해당 페이지를 가져오는 URL 매핑이 있는지 config/urls.py파일을 찾아본다.
하지만 우리는 /pybo/ 페이지에 해당하는 URL매핑을 장고에 등록하지 않아서 그렇다.
그래서 장고는 /pybo/ 페이지를 찾을 수 없다고 메시지를 보낸 것이다.

---

## config/urls.py 수정하기

~~~ python
from django.contrib import admin
from django.urls import path
from pybo import views # 추가됨

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', views.index), # 추가됨
]
~~~
이렇게 추가하는 행위를 __'URL 매핑을 추가한다'__ 라고 말할 것이다.

config/urls.py은 페이지 요청시 가장 먼저 호출되며, 요청 URL과 뷰함수를 1:1로 연결해줌

__pybo/ URL이 요청되면 views.index를 호출하라는 매핑을 urlpatterns에 추가하였다.__
__views.index는 view.py파일의 index 함수를 의미한다.__

웹 브라우저 주소창에 localhost:8000/pybo라고 입력하면 장고가 자동으로 localhost:8000/pybo/와 같이 /를 붙여준다.

그럼 다시 한번 /pybo/에 접속하면 '사이트를 연결할 수 없음'라고 오류가 뜬다.

그 이유는 URL 매핑에 추가한 뷰 함수 views.index가 없기 때문이다.

---

## views.py 수정하기

pybo/views.py 파일에 index함수를 추가해보자.

~~~python
from django.http import HttpResponse

def index(request):
  return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
~~~

return문에 사용된 HttpResponse는 페이지 요청에 대한 응답을 할 때 사용하는 장고 클래스이다.

여기서 HttpResponse에 "안녕하세요 pybo에 오신것을 환영합니다."라는 문자열을 전달하여 이 문자열이 웹 브라우저에 그대로 출력되도록 만들었다.

index 함수의 매개변수 request는 HTTP요청 객체이다.

이후 다시 접속하면 웹브라우저에 "안녕하세요 pybo에 오신것을 환영합니다."라는 문자열이 출력된다.

---

## URL 분리하기

config/urls.py 파일을 다시 한번 살펴보자.

아까 얘기했듯 pybo 앱 관련 파일은 대부분 pybo 디렉터리에 있다. 하지만 config/urls.py 파일은 pybo 디렉터리에 없다.

그러므로 pybo앱에 URL 매핑을 추가하려면 pybo 디렉터리가 아닌 config 디렉터리에 있는 urls.py 파일을 수정해야 한다.

-> 이 방법은 pybo앱에서만 사용하는 URL 매핑을 config/urls.py 파일에 계속 추가하는 것은 좋은 방법이 아니다.

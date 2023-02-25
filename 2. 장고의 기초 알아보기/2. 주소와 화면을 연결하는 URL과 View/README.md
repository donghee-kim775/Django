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

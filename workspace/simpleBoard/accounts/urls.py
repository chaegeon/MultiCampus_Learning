from django.urls import path
from django.urls.conf import include
from . import views
# .은 현재경로 -> 같은 경로의 views를 가져오라는 뜻

#127,0.0.1:8000/profile 까지 온 것.
# 그 다음은 어디로 가지? 는 이 밑에서 설정
# profile 이후의 경로를 지정해주는 곳
urlpatterns = [
    path( 'login/', views.login), # => 127.0.0.1:8000/board/login
]
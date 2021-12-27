from django.urls import path
from django.urls.conf import include
from . import views
# .은 현재경로 -> 같은 경로의 views를 가져오라는 뜻

#127,0.0.1:8000/board 까지 온 것.
# 그 다음은 어디로 가지? 는 이 밑에서 설정
# board 이후의 경로를 지정해주는 곳
urlpatterns = [
    path('', views.index),
    path('list/', views.list ), # 127.0.0.1:8000/board
    # '' 는 board까지 썼을 때 화면은 얘가 담당해준다는 뜻
    # views의 index()를 호출
    path( 'write/', views.write) # => 127.0.0.1:8000/board/login

]
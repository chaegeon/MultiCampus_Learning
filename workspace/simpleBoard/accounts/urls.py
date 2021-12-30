from django.contrib import auth
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import TemplateView
from . import views
from board import views as board_views
# .은 현재경로 -> 같은 경로의 views를 가져오라는 뜻
from django.contrib.auth import views as auth_views
# auth에서 제공하는 로그인 처리 기능들을 사용하려고 함
# 이 views는 auth의 views

#127,0.0.1:8000/profile 까지 온 것.
# 그 다음은 어디로 가지? 는 이 밑에서 설정
# profile 이후의 경로를 지정해주는 곳
urlpatterns = [
    #path('', views.login), # => 127.0.0.1:8000/profile/login
 
    path( 'createUser/', views.createUser),
    path( 'signUp/', views.signup),
    path( 'signIn/', auth_views.LoginView.as_view(template_name='accounts/signin.html')), 
# signin의 views는 우리가 만든 views 말고 auth에 있는 view를 쓰자
# 거기엔 이미 로그인 기능들이 들어있음
    path('signOut/', auth_views.LogoutView.as_view()), # LoginView가 아니라 LogoutView임 주의
]


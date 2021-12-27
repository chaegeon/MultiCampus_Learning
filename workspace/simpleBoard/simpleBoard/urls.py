"""simpleBoard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# 127.0.0.1:8000 까지만 받고, 그 뒤의 경로를 지정
urlpatterns = [

    path('admin/', admin.site.urls),
    path('board/', include('board.urls')), 
    path('profile/', include('accounts.urls')),
    # 세부 경로 설정
    # include('board/urls') : 127.0.0.1:8000/board/?
    # ?부터 세부경로를 담당하는 파일로 이동하라는 의미
    # 카테고리를 묶는 개념? 보드라고 묶을 테니 그 하위는 보드 밑 urls.py에서 지정해라
]

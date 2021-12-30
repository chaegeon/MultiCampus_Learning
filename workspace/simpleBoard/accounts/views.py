from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your views here.

#def signin(request):
#  return render(request, 'accounts/signin.html')
# 이거 안 쓸 거

def signup(request):
  return render(request, 'accounts/signup.html')

def createUser(request):
  id = request.POST['id']
  pw = request.POST['pw']
  user = User(username=id, password=make_password(pw))
  user.save()               # 이렇게 해야 일반 user도 해쉬가 부여됨(?)
                          # 관리자페이지에서 user 누르면 username 밑에 hash가 뜸
  return HttpResponseRedirect(reverse('list'))

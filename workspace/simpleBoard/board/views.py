from typing import ContextManager
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls.base import reverse

from .models import Board
# .은 현재 패키지라는 뜻 
# 현재디렉토리의 모델스라는 모듈의 Board를 import


# Create your views here.
#def indes(request):
#  return HttpResponse('board의 메인화면')
def index( request):
  # DB의 board 테이블의 모든내용을 가져온다
  rows = Board.objects.all()
  print(rows)
  # print( rows) # 저장하고 브라우저 리프레쉬 하면 터미널에 쿼리셋 뜸
  content = {'rows':rows}
  # 딕셔너리 형태로 만들어서 통째로
  return render(request, 'board/list.html', content)

  #return HttpResponse('연결 완료')
#def list( request ):
  #return render(request, '연결이 완료되었습니다.')
  # return 
  

#def index( request ):
  # DB의 내용을 브라우저에 전달하기 위한 코드를 추가
  #todos = Board.objects.all() # 테이블 내의 모든 내용을 조회
  #content = {'':}
  #return render( request, 'board/list.html', content) 


def login(request):
  return render(request, 'board/login.html')

def write(request):
  return render(request, 'board/write.html')

def create(request):
  #데이터를 전달받는다
  #print(request.POST['createDate'])
  #print(request.POST['user'])
  #print(request.POST['subject'])
  #print(request.POST['content'])
  # 이렇게 print해놓고 브라우저에서 글작성하면 터미널에도 보임
  # 이걸 DB에 넣을 거임

  new = Board(
    createDate = request.POST['createDate'],
    writer = request.POST['user'],
    subject = request.POST['subject'],
    content = request.POST['content'],
    )
  new.save()

  return HttpResponseRedirect(reverse('list'))
    # 글작성 하고 작성완료 뜬 후 보드 페이지로 돌아가게

def delete( request ):
  #print(request.POST['id'])
  b = Board.objects.get(id= request.POST['id'])
  b.delete()
  return HttpResponseRedirect(reverse('list')) 

def update( request):
  #print('id', request.GET['id']) #list에서 id를 보내면 여기서 id를 받아옴
  
  #수정하려면 기존 내용을 가져와야 수정하지
  post = Board.objects.get(id = request.GET['id'])
  content = {'post': post} # 가져와서 콘텐트에 넣어
  return render( request, 'board/update.html', content)

def modify(request): # write? create와의 차이점은 객체를 만들지 않아. 기존의 객체를 가져옴
  post = Board.objects.get(id=request.POST['id'])
  post.createDate = request.POST['createDate']
  post.writer = request.POST['user']
  post.subject = request.POST['subject']
  post.content = request.POST['content']
  post.save()

  return HttpResponseRedirect( reverse('list'))

def view(request):
  post = Board.objects.get(id=request.GET['id'])
  content = {'post':post}
  return render(request, 'board/view.html', content)

def view(request):
  #user = Board.objects.get()
  print(request)
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# render는 이미 임포트 되어있기 때문에 그냥 함수만 정의해 주자

# 미리 만들어진 model을 가져오도록 한다
from .models import *

#insdex페이지로 돌아가기 위한 reverse를 임포트한다
from django.urls import reverse

# Create your views here.
def index( request ):
  # DB의 내용을 브라우저에 전달하기 위한 코드를 추가
  todos = Todo.objects.all() # 테이블 내의 모든 내용을 조회
  content = {'todos':todos}
  return render( request, 'my_to_do_app/index.html', content) 

def createTodo( request):
  # URL과 view가 잘 연결되었는지 확인하기 위해서 아래와 같은 코드 이용
  # return HttpResponse('create Todo를 할거')

  # 사용자가 입력한 할 일을 잘 받아 오는지 확인
  # (index.html에서 보면 44번째줄 정도에 있음)
  # 입력값 전달은 POST방식으로 'todoContent' 변수를 통해서 전달이 될 것

  # user_input_str = request.POST['todoContent']
  # return HttpResponse(f'사용자가 입력한 값: {user_input_str}')

  user_input_str = request.POST['todoContent']
  # models.py에서 정의된 클래스를 이용해서 전달받은 갑을 DB에 저장한다
  new_todo = Todo( content = user_input_str )
  new_todo.save ()
    # 투두객체를 생성할 떄 콘텐트를 보내면 해당 객체를 저장
  return HttpResponseRedirect(reverse('index'))
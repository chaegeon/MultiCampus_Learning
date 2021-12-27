
from django.shortcuts import render, HttpResponse

# Create your views here.
#def indes(request):
#  return HttpResponse('board의 메인화면')
def index( request):
  #return HttpResponse('연결 완료')
#def list( request ):
  #return render(request, '연결이 완료되었습니다.')
  # return 
  return render(request, 'board/list.html')



def write(request):
  return render(request, 'board/write.html')

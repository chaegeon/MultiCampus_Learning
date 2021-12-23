from django.urls import path, include
# view 와 연결
from. import views

urlpatterns = [
    path('', views.index, name = 'index'),  
      
    # url: http://127,0,0,1:8000/index.html
    # http에서 GET/index.html HTTP/1.1 요청을 할거야
    # 이걸 최상위 URLconf 가 받음-> path('', include('app.url')) )
    # URLconf는 받은 것중에서 index.html 이 부분을 찾아(정확하게는 '' 이 부분을 찾음)
    #  '' 부분에 매치되는 걸 찾아 하위 URLconf랑 연결해
    # view랑 연결해 놓음. view는 컨트롤 역할을 함
    # view는 url과 tamplets 사이에서 중재역할
    # 이 때, view에 정의된 index는 view에 정의된 함수
    # view에 인덱스 함수를 달아주면 된다?
    # 이제 view를 통해서 URL과 tamplets 화면을 연결해주면, 원하는 화면을 볼 수 있음
    
    # createTodo에 대한 YRL요청과 view를 연결해 준다.
    # 아까 인덱스함수랑 연결해준 것처럼 createTodo 함수랑 연결해 준것
    # 이제 views.py 가서 createTodo 함수 정의하러
    path('createTodo/', views.createTodo),
]


from django.contrib import admin #만약 여기가 오류가 난다면, 가상환경과 인터프리터가 맞게 됐는지 확인
from .models import Board


# Register your models here.

class BoardAdmin( admin.ModelAdmin):
    list_display = ('createDate', 'user', 'subject')
    # 관리자 페이지에서 화면에 보여지는 목록을 설정

    list_display_links = ['subject']
    # 링크를 새로 정의
    # 지금은 날짜를 클릭해야 해당 글로 들어가지는데
    # 제목을 클릭해서 해당 글의 상세페이지로 이동할 수 있도록

admin.site.register(Board, BoardAdmin) 
# import 하고 이렇게 등록만 시켜주면
# 관리자 페이지(admin)에 Board를 관리할 수 있는 탭이 생김
from django.contrib import admin
from .models import Board


# Register your models here.
admin.site.register(Board)
# import 하고 이렇게 등록만 시켜주면
# 관리자 페이지(admin)에 Board를 관리할 수 있는 탭이 생김
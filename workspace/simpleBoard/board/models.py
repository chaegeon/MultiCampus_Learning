from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# ORM(Object Realation Mapping)
class Board( models.Model): # models모듈 내의 Model클래스를 상속받아 새로운 클래스 Board를 정의
    user = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete~ : 유저가 삭제되면 그 유저에 해당하는 보드도 삭제하게 하는 설정
    createDate = models.DateField()
    # writer = models.CharField(max_length=128) # 결국 Username이라 없어도 되긴 한데..,,
    subject = models.CharField(max_length=255)
    content = models.TextField()

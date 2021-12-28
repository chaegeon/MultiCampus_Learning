from django.db import models

# Create your models here.
# ORM(Object Realation Mapping)
class Board( models.Model): # models모듈 내의 Model클래스를 상속받아 새로운 클래스 Board를 정의
    createDate = models.DateField()
    writer = models.CharField(max_length=128)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    # 4개의 컬럼 지정

from django.db import models

# Create your models here.
# ORM(Object Realation Mapping)
class Board( models.Model): # 모델클래스 상속
    createDate = models.DateField()
    writer = models.CharField(max_length=128)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    # 4개의 컬럼 지정

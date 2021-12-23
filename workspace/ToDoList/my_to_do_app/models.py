from django.db import models

# Create your models here.
# 클래스의 이름이 모델(테이블)의 이름이 된다
class Todo( models.Model): 
# models모듈 내의 Model클래스를 상속받아 새로운 클래스 Todo를 정의
    # content 컬럼을 정의
    # 이 content 컬럼의 타입은 문자타입.  최대 길이는 255바이트
    content = models.CharField(max_length=255)
    


from django.db import models

# Create your models here.

class Ikkuuu( models.Model):
    creatDate = models.DateField()
    writer = models.CharField(max_length=128)
    subject = models.CharField(max_length=255)
    content = models.TextField()
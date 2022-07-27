from django.db import models

# Create your models here.
class User(models.Model):
    """用户基本信息"""
    username = models.CharField('用户名', max_length=128)
    password = 

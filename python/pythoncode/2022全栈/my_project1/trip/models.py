from django.db import models

# Create your models here.
class Sight(models.Model):
    """景点表"""
    name = models.CharField('景点名称', max_length=64)
    address = models.CharField('景点地址', max_length=64)

class Order(models.Model):
    """订单表"""
    sn = models.CharField('订单号', max_length=64)
    amount = models.FloatField('订单金额')

class SightComment(models.Model):
    """景点评论"""
    content = models.CharField('评论内容', max_length=512)
    score = models.FloatField('分数', default=5)

class OrderComment(models.Model):
    """订单评论"""
    content = models.CharField('评论内容', max_length=512)
    score = models.FloatField('分数', default=5)

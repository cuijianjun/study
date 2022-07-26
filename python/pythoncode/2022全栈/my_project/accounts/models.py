from django.db import models

# Create your models here.

class CommomModel(models.Model):
    """自定义模型的基类"""
    create_at = models.DateTimeField('注册时间', auto_now_add=True)
    updated_at = models.DateTimeField('最后修改时间', auto_now=True)
    class Meta:
        """抽象类，这个类，并不会生成对应的数据库表"""
        abstract = True


class User(CommomModel):
    """用户模型"""
    name = models.CharField('姓名', max_length=64)
    sex = models.CharField('性别', max_length=1, choices=(
        ('1', '帅哥'),
        ('0', '美女')
    ), default='1')
    
    age = models.PositiveIntegerField('年龄', default=0)
    username= models.CharField('用户名', max_length=64, unique=True)
    password = models.CharField('备注', max_length=256, null=True, blank=True)
    remark = models.CharField('备注', max_length=64, null=True, blank=True)
    email = models.EmailField('用户的邮箱', max_length=64, null=True,blank=True)

    
    
    collect_ques = models.ManyToManyField('Question')
    class Meta:
        db_table = 'user'


class Manager(User):
    class Meta:
        proxy = True
class Profile(CommomModel):
    """用户详细信息"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField('昵称', max_length=64)

class Question(CommomModel):
    """问题"""
    name = models.CharField('问题名称', max_length=64)

class Answer(CommomModel):
    """答案"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
    related_name='answers',
    verbose_name='关联的问题')
    name = models.CharField('答案内容', max_length=256)

class Classify(models.Model):
    """
        分类
        1. 酒水
            2. 啤酒
            3. 白酒
    """
    name = models.CharField('名称', max_length=64)
    parent = models.ForeignKey('self', related_name='children',
    on_delete=models.CASCADE)

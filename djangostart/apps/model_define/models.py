from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    """快速上手示例"""
    # 定义字段
    name = models.CharField(max_length=30, verbose_name='分类名称')
    desc = models.CharField(max_length=255, default=None, verbose_name='分类描述')
    index = models.IntegerField(default=999, verbose_name='分类的排序')

    # 设置元数据（设置查询和展示的输出）
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']
        db_table = "category"

    # 类的魔术方法，返回一个友好的显示
    def __str__(self):
        return self.name
import random
def func01(self):
    return random.randint(1000,2000)

class Student(models.Model):
    """
    primary_key :设置主键
    如果定义了主键，就不会再创建名为id的主键字段了
    verbose_name
    """
    SEX_CHOICES = (
        (0, '男'),
        (1, '女'),
        (2, '保密'),
    )


    #AutoField:自增型字段（值增量） =》 int
    student_id = models.AutoField(primary_key=True)
    #max_length将在数据库中和Django表单中起验证作用，用来限定字段的长度
    username =models.CharField(max_length=10)
    #用于大文本数据
    desc = models.TextField(verbose_name="个人简介",help_text="这是个人简介，请不要超过100个字")
    sex = models.IntegerField(verbose_name="性别", choices=SEX_CHOICES)  #0 => 男  1 =》 女
    #录入时间
    insert_time = models.DateTimeField(auto_now_add=True)
    #更新时间
    update_time = models.DateTimeField(auto_now=True)
    #成绩
    English_score = models.FloatField(verbose_name="英语成绩")
    #学费（跟钱相关的，一定要用这个字段类型）
    schooling = models.DecimalField(max_digits=7,decimal_places=2, verbose_name="学费", default=6000)
    #邮箱
    email = models.EmailField(verbose_name="邮箱")
    #最后登录的IP
    last_login_ip = models.GenericIPAddressField(verbose_name="最后登录的IP")
    #当前登录状态
    is_login = models.BooleanField()
    #NullBooleanField的默认值是Null
    is_login2 = models.NullBooleanField()
    avator = models.ImageField(upload_to="avator/", default='avator/default.png', verbose_name="用户头像")
    #null=False => 数据库 =》这是一个必填项
    allow_null = models.CharField(max_length=10, verbose_name="允许为空的字段",null=True)
    #blank=False => 表单 =》 这是一个必填项
    allow_blank = models.CharField(max_length=10, verbose_name="允许为空的字段", blank=True)
    #注意事项：用null跟blank 要同时设置，要么都为True，要么都为False
    select = models.CharField(max_length=10, db_column="choices")












    def __str__(self):
        return self.username

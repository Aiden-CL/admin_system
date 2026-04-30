from django.db import models


class Member(models.Model):
    """注册人员信息"""

    GENDER_CHOICES = [
        ('M', '男'),
        ('F', '女'),
    ]

    name = models.CharField('姓名', max_length=50)
    phone = models.CharField('手机号', max_length=20, unique=True)
    gender = models.CharField('性别', max_length=1, choices=GENDER_CHOICES, blank=True, default='')
    id_number = models.CharField('身份证号', max_length=18, blank=True, default='')
    email = models.EmailField('邮箱', blank=True, default='')
    address = models.CharField('地址', max_length=200, blank=True, default='')
    birthday = models.DateField('出生日期', null=True, blank=True)
    remark = models.TextField('备注', blank=True, default='')
    created_at = models.DateTimeField('注册时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '注册人员'
        verbose_name_plural = '注册人员'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} ({self.phone})'

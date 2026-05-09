from django.contrib.auth.models import AbstractUser
from django.db import models


class AdminUser(AbstractUser):
    """自定义管理员用户模型"""

    phone = models.CharField('手机号', max_length=20, blank=True, default='')
    avatar = models.ImageField('头像', upload_to='avatars/', blank=True, default='')
    position = models.CharField('职位', max_length=100, blank=True, default='')
    department = models.CharField('部门', max_length=100, blank=True, default='')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    updated_at = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '管理员用户'
        verbose_name_plural = '管理员用户'
        ordering = ['-date_joined']

    def __str__(self):
        return self.get_full_name() or self.username


class OperationLog(models.Model):
    """操作日志"""

    user = models.ForeignKey(
        AdminUser,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='操作用户',
    )
    action = models.CharField('操作类型', max_length=50)
    target = models.CharField('操作对象', max_length=200, blank=True, default='')
    detail = models.TextField('操作详情', blank=True, default='')
    ip_address = models.GenericIPAddressField('IP地址', null=True, blank=True)
    created_at = models.DateTimeField('操作时间', auto_now_add=True)

    class Meta:
        verbose_name = '操作日志'
        verbose_name_plural = '操作日志'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user} - {self.action} - {self.created_at}'

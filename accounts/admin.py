from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AdminUser, OperationLog


@admin.register(AdminUser)
class AdminUserAdmin(UserAdmin):
    list_display = [
        'username', 'email', 'first_name', 'last_name',
        'department', 'position', 'is_active', 'date_joined',
    ]
    list_filter = ['is_active', 'is_staff', 'is_superuser', 'department']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    fieldsets = UserAdmin.fieldsets + (
        ('扩展信息', {'fields': ('phone', 'avatar', 'position', 'department')}),
    )


@admin.register(OperationLog)
class OperationLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'action', 'target', 'ip_address', 'created_at']
    list_filter = ['action', 'created_at']
    search_fields = ['user__username', 'target', 'detail']
    readonly_fields = [
        'user', 'action', 'target', 'detail', 'ip_address', 'created_at',
    ]

from django.contrib import admin

from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'gender', 'email', 'address', 'created_at']
    list_filter = ['gender', 'created_at']
    search_fields = ['name', 'phone', 'id_number', 'email']
    readonly_fields = ['created_at', 'updated_at']

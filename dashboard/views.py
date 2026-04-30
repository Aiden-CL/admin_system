from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.models import OperationLog

User = get_user_model()


@login_required
def index(request):
    """仪表盘首页"""
    context = {
        'total_users': User.objects.count(),
        'active_users': User.objects.filter(is_active=True).count(),
        'staff_users': User.objects.filter(is_staff=True).count(),
        'superusers': User.objects.filter(is_superuser=True).count(),
        'recent_logs': OperationLog.objects.select_related('user').all()[:10],
    }
    return render(request, 'dashboard/index.html', context)

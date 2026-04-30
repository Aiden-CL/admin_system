from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

from accounts.models import OperationLog
from members.models import Member

User = get_user_model()


@login_required
def index(request):
    """仪表盘首页"""
    today = timezone.now().date()
    context = {
        'total_users': User.objects.count(),
        'active_users': User.objects.filter(is_active=True).count(),
        'total_members': Member.objects.count(),
        'today_members': Member.objects.filter(created_at__date=today).count(),
        'recent_logs': OperationLog.objects.select_related('user').all()[:10],
    }
    return render(request, 'dashboard/index.html', context)

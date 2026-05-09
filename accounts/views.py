from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from .forms import (
    AdminUserCreateForm,
    AdminUserUpdateForm,
    LoginForm,
    ProfileForm,
)
from .models import OperationLog

User = get_user_model()


def is_superuser(user):
    return user.is_superuser


class AdminLoginView(LoginView):
    """管理员登录视图"""

    template_name = 'accounts/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        OperationLog.objects.create(
            user=user,
            action='登录',
            target='系统',
            detail=f'用户 {user.username} 登录系统',
            ip_address=self.request.META.get('REMOTE_ADDR'),
        )
        return redirect(self.get_success_url())


class AdminLogoutView(LogoutView):
    """管理员登出视图"""

    next_page = reverse_lazy('accounts:login')


@login_required
def profile_view(request):
    """个人资料视图"""
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, '个人资料更新成功')
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})


@login_required
@user_passes_test(is_superuser)
def user_list_view(request):
    """用户列表视图"""
    users = User.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})


@login_required
@user_passes_test(is_superuser)
def user_create_view(request):
    """创建用户视图"""
    if request.method == 'POST':
        form = AdminUserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            OperationLog.objects.create(
                user=request.user,
                action='创建用户',
                target=user.username,
                detail=f'创建用户 {user.username}',
                ip_address=request.META.get('REMOTE_ADDR'),
            )
            messages.success(request, f'用户 {user.username} 创建成功')
            return redirect('accounts:user_list')
    else:
        form = AdminUserCreateForm()
    return render(request, 'accounts/user_form.html', {
        'form': form,
        'title': '创建用户',
    })


@login_required
@user_passes_test(is_superuser)
def user_update_view(request, pk):
    """编辑用户视图"""
    user_obj = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = AdminUserUpdateForm(request.POST, instance=user_obj)
        if form.is_valid():
            form.save()
            OperationLog.objects.create(
                user=request.user,
                action='编辑用户',
                target=user_obj.username,
                detail=f'编辑用户 {user_obj.username}',
                ip_address=request.META.get('REMOTE_ADDR'),
            )
            messages.success(request, f'用户 {user_obj.username} 更新成功')
            return redirect('accounts:user_list')
    else:
        form = AdminUserUpdateForm(instance=user_obj)
    return render(request, 'accounts/user_form.html', {
        'form': form,
        'title': '编辑用户',
    })


@login_required
@user_passes_test(is_superuser)
def user_delete_view(request, pk):
    """删除用户视图"""
    user_obj = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        username = user_obj.username
        OperationLog.objects.create(
            user=request.user,
            action='删除用户',
            target=username,
            detail=f'删除用户 {username}',
            ip_address=request.META.get('REMOTE_ADDR'),
        )
        user_obj.delete()
        messages.success(request, f'用户 {username} 已删除')
        return redirect('accounts:user_list')
    return render(request, 'accounts/user_confirm_delete.html', {
        'user_obj': user_obj,
    })


@login_required
@user_passes_test(is_superuser)
def operation_log_view(request):
    """操作日志视图"""
    logs = OperationLog.objects.select_related('user').all()[:100]
    return render(request, 'accounts/operation_log.html', {'logs': logs})

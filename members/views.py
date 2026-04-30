from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from accounts.models import OperationLog

from .forms import MemberForm
from .models import Member


@login_required
def member_list(request):
    """注册人员列表"""
    members = Member.objects.all()
    return render(request, 'members/member_list.html', {'members': members})


@login_required
def member_create(request):
    """注册人员信息录入"""
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save()
            OperationLog.objects.create(
                user=request.user,
                action='注册人员',
                target=member.name,
                detail=f'注册人员 {member.name}（{member.phone}）',
                ip_address=request.META.get('REMOTE_ADDR'),
            )
            messages.success(request, f'人员 {member.name} 注册成功')
            return redirect('members:member_list')
    else:
        form = MemberForm()
    return render(request, 'members/member_form.html', {
        'form': form,
        'title': '注册人员',
    })


@login_required
def member_detail(request, pk):
    """注册人员详情"""
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'members/member_detail.html', {'member': member})


@login_required
def member_update(request, pk):
    """编辑注册人员信息"""
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            OperationLog.objects.create(
                user=request.user,
                action='编辑人员',
                target=member.name,
                detail=f'编辑人员 {member.name}（{member.phone}）',
                ip_address=request.META.get('REMOTE_ADDR'),
            )
            messages.success(request, f'人员 {member.name} 信息更新成功')
            return redirect('members:member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'members/member_form.html', {
        'form': form,
        'title': '编辑人员信息',
    })


@login_required
def member_delete(request, pk):
    """删除注册人员"""
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        name = member.name
        OperationLog.objects.create(
            user=request.user,
            action='删除人员',
            target=name,
            detail=f'删除人员 {name}（{member.phone}）',
            ip_address=request.META.get('REMOTE_ADDR'),
        )
        member.delete()
        messages.success(request, f'人员 {name} 已删除')
        return redirect('members:member_list')
    return render(request, 'members/member_confirm_delete.html', {'member': member})

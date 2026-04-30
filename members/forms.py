from django import forms

from .models import Member


class MemberForm(forms.ModelForm):
    """注册人员表单"""

    class Meta:
        model = Member
        fields = [
            'name', 'phone', 'gender', 'id_number',
            'email', 'address', 'birthday', 'remark',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入姓名'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入手机号'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入身份证号'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '请输入邮箱'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入地址'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'remark': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': '备注信息'}),
        }

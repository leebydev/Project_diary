from django import forms
from users.models import Member
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


# 장고의 ModelForm을 상속 받아서 사용
class LoginForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['username', 'password']

        labels = {
            'username': '사용자이름',
            'password': '비밀번호'
        }

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '사용자 이름을 입력 하세요'
                }
            ),

            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '비밀번호를 입력 하세요'
                }
            )
        }


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        models = get_user_model()
        fields = UserCreationForm.Meta.fields


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta(UserCreationForm.Meta):
        model = Member
        fields = ("username", "password1", "password2", "email")

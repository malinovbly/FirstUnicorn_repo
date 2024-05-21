from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "autofocus": True,
            'class': 'form-control',
            'placeholder': 'Введите ваше имя пользователя',
        })
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "autofocus": "current-password",
            'class': 'form-control',
            'placeholder': 'Введите ваш пароль',
        })
    )


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "patronymic",
            "username",
            "email",
            "password1",
            "password2",
            "city",
            "profession",
            "work_experience",
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    patronymic = forms.CharField(required=False)
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    city = forms.CharField()
    profession = forms.CharField()
    work_experience = forms.CharField()


class ProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            "image",
            "username",
            "first_name",
            "last_name",
            "patronymic",
            "email",
            "city",
            "profession",
            "work_experience",
            "self_info",
        )

    
    image = forms.ImageField(required=False)
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    patronymic = forms.CharField(required=False)
    email = forms.CharField()
    city = forms.CharField()
    profession = forms.CharField()
    work_experience = forms.CharField()
    self_info = forms.CharField(required=False)

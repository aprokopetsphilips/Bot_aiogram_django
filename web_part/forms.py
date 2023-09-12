from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from bot.models import Command


class UserFilterForm(forms.Form):
    username = forms.CharField(max_length=100, required=False, label='Имя пользователя')



class CommandForm(forms.ModelForm):
    class Meta:
        model = Command
        fields = ['name', 'keyword', 'description', 'negative']

    def __init__(self, *args, **kwargs):
        super(CommandForm, self).__init__(*args, **kwargs)
        # Добавляем атрибут disabled для поля name
        self.fields['name'].widget.attrs['readonly'] = True

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
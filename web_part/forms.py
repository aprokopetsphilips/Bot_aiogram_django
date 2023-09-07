from django import forms

class UserFilterForm(forms.Form):
    username = forms.CharField(max_length=100, required=False, label='Имя пользователя')
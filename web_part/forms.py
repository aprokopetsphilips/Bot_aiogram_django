from django import forms

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
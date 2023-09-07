from django.shortcuts import render
from django.views.generic import ListView

from bot.models import Chat
from .forms import UserFilterForm


# Create your views here.


class ChatListView(ListView):
    model = Chat
    template_name = 'web_part/chat_list.html'
    # form_class = FeedbackForm
    # template_name = 'feedback/feedback.html'
    # success_url = '/done'
    context_object_name = 'All_people'  # имя которое используем в шаблоне
    form = UserFilterForm()

    def get_queryset(self):
        queryset = super().get_queryset()  # Получитаем исходный QuerySet
        username = self.request.GET.get('username')  # Получитаем значение из формы

        if username:
            # Применить фильтр по имени пользователя, если указано
            queryset = queryset.filter(account__user_name__icontains=username)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form  # Передает форму в контекст
        return context
# get_queryset(self): Этот метод переопределен для определения QuerySet (набора объектов) модели Chat, который будет отображаться на странице. Он выполняется,
# когда вы запрашиваете страницу, и его результат будет отображаться на странице.
# queryset = super().get_queryset(): Сначала он вызывает метод get_queryset родительского класса (в данном случае, класса ListView) для получения исходного QuerySet
# всех объектов модели Chat.
# username = self.request.GET.get('username'): Затем он извлекает значение параметра username из GET-запроса, который был передан из формы. Это значение будет
# использоваться для фильтрации данных.
# if username:: Далее он проверяет, было ли передано значение username. Если значение существует (то есть было введено в форме), то выполняется следующая строка.
# queryset = queryset.filter(account__user_name__icontains=username): Эта строка фильтрует QuerySet queryset, чтобы оставить только объекты, у которых поле account
# (связанное с моделью Account) имеет user_name, содержащее введенное имя пользователя. Фильтр происходит с использованием icontains, что означает, что фильтрация
# происходит без учета регистра букв (например, "John" и "john" будут считаться одним и тем же именем).
# return queryset: Наконец, метод возвращает измененный QuerySet, который будет использоваться для отображения на странице.
# get_context_data(self, **kwargs): Этот метод также переопределен для добавления дополнительной информации в контекст шаблона, помимо основных данных (QuerySet).
# В данном случае, он добавляет форму UserFilterForm в контекст.
# context = super().get_context_data(**kwargs): Сначала он вызывает метод get_context_data родительского класса (в данном случае, класса ListView) для получения
# базового контекста.
# context['form'] = self.form: Затем он добавляет форму self.form (которая создается из класса UserFilterForm) в контекст под ключом 'form'.
# return context: Наконец, метод возвращает контекст, который будет доступен в вашем шаблоне для отображения данных и формы.
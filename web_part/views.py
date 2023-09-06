from django.shortcuts import render
from django.views.generic import ListView

from bot.models import Chat


# Create your views here.


class ChatListView(ListView):
    model = Chat
    template_name = 'web_part/chat_list.html'
    # form_class = FeedbackForm
    # template_name = 'feedback/feedback.html'
    # success_url = '/done'
    context_object_name = 'All_people'  # имя которое используем в шаблоне
"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from web_part.views import ChatListView, command_list, edit_command, create_command

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ChatListView.as_view(), name='home'),
    path('command_list/', command_list, name='command_list'),
    path('edit_command/<int:command_id>/', edit_command, name='edit_command'),
    path('create_command/', create_command, name='create_command'),

]

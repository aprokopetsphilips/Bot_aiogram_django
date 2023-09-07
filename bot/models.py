import datetime

from django.db import models
# Create your models here.
from django.db import models

class Account(models.Model):
    user_num = models.IntegerField()
    user_name = models.TextField(blank=True)
    def __str__(self):
        return self.user_name

class Chat(models.Model):
    message = models.TextField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    time_chat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message



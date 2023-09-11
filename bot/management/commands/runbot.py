import os

import django
from django.core.management import BaseCommand

from bot.handlers import client, other

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
import django
django.setup()
from bot.create_bot import dp
from aiogram import executor  # для запуска бота



async def on_startup(_):
    print('hello')


client.register_handler(dp)
other.register_handler_other(dp)


class Command(BaseCommand):
    help = 'RUN COMMAND: python manage.py runbot'

    def handle(self, *args, **options):
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


# import os
#
# import django
# from django.core.management import BaseCommand
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')
# import django
# django.setup()
# from create_bot import dp
# from aiogram import executor  # для запуска бота
#
# from handlers import client, other
#
#
# async def on_startup(_):
#     print('hello')
#
#
#
# client.register_handler(dp)
# other.register_handler_other(dp)
#
#
# # executor.start_polling(dp,
# #                        skip_updates=True, on_startup=on_startup)  # executor- модуль в aiogram.utils, который предоставляет методы для запуска бота.
# # # start_polling(dp, skip_updates=True): Этот метод запускает опрос бота, принимая два аргумента:
# # # dp: Объект Dispatcher (диспетчер), который управляет обработкой входящих событий и их распределением по соответствующим обработчикам.
# # # skip_updates=True: Этот параметр указывает, что необходимо пропустить обработку старых обновлений, которые могли накопиться в момент запуска бота.
#
#
# class Command(BaseCommand):
#     help = 'RUN COMMAND: python manage.py runbot'
#
#     def handle(self, *args, **options):
#         executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
#

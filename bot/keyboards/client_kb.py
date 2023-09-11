from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot.models import Command
buttons = []
for elem in Command.objects.all():
    buttons.append(KeyboardButton(f'/{elem.keyword}'))

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(*buttons)
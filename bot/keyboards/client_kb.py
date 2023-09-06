from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/help')
b3 = KeyboardButton('/weather')
b4 = KeyboardButton('/news')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).add(b2).add(b3).add(b4)
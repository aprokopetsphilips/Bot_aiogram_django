import json
import string
from aiogram import types, Dispatcher


# определение функции удаления мата в сообщениях
async def echo_send(message: types.Message):
    if {x.lower().translate(str.maketrans('', '', string.punctuation)) for x in message.text.split(' ')}.intersection(set(json.load(open('cenz.json','r', encoding='utf-8')))):
        await message.reply('Привет, дорогой друг!Мат здесь запрещен.')
        await message.delete()

def register_handler_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
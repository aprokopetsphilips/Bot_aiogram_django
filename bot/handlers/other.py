import json
import string
from aiogram import types, Dispatcher
from bot.create_bot import dp


# @dp.message_handler()
async def echo_send(message: types.Message):  # используем аннотацию типов
    if {x.lower().translate(str.maketrans('', '', string.punctuation)) for x in message.text.split(' ')}.intersection(set(json.load(open('cenz.json','r', encoding='utf-8')))):
        await message.reply('Привет, дорогой друг!Мат здесь запрещен.')
        await message.delete()
    # await - возможность ожидания. Берем текст принятого сообщения и возвращаем его
    # await message.reply(message.text) # отправляет в ответ на сообщение
    # await bot.send_message(message.from_user.id, message.text) # пишет пользователю в личку, но только если пользователь сам первый написал боту

def register_handler_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
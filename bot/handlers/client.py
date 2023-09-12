# Импорт необходимых модулей и библиотек
import json
import os
import string
from datetime import datetime
import requests
from bot.create_bot import bot, API
from aiogram import types, Dispatcher
from bot.keyboards.client_kb import kb_client
from bot.models import Account, Chat, Command
from bot.news import get_fresh_news
from asgiref.sync import sync_to_async
from my_project.settings import BASE_DIR

# Определение функции для получения описания команды (асинхронная)
@sync_to_async
def get_command_description(command_name):
    try:
        return Command.objects.get(name=command_name).description
    except Exception as e:
        print(e)

# Определение функции для получения отрицательного описания команды (асинхронная)
@sync_to_async
def get_negative_command_description(command_name):
    try:
        return Command.objects.get(name=command_name).negative
    except Exception as e:
        print(e)

# Определение обработчика команды /start
async def command_start(message: types.Message):
    try:
        response_message = await get_command_description('command_start')
        await bot.send_message(message.from_user.id, response_message, reply_markup=kb_client)
    except:
        response_message = await get_negative_command_description('command_start')
        await message.reply(message.from_user.id, response_message, reply_markup=kb_client)
    await insert_data(message.from_user.id, message.from_user.full_name, message.text)
    await insert_data(message.from_user.id, message.from_user.full_name, response_message)

# Определение обработчика команды /help
async def command_help(message: types.Message):
    try:
        response_message = await get_command_description('command_help')
        await bot.send_message(message.from_user.id, response_message)
        await insert_data(message.from_user.id, message.from_user.full_name, message.text)
        await insert_data(message.from_user.id, message.from_user.full_name, response_message)
    except:
        pass

# Определение функции для получения погоды
async def get_weather(message: types.Message):
    response_message = await get_command_description('get_weather')
    print(response_message)
    await bot.send_message(message.from_user.id, response_message)
    await insert_data(message.from_user.id, message.from_user.full_name, message.text)

# Определение функции для ответа на запрос погоды
async def answer_weather(message: types.Message):
    cenz_json_path = os.path.join(BASE_DIR, 'bot', 'cenz.json')
    if {x.lower().translate(str.maketrans('', '', string.punctuation)) for x in message.text.split(' ')}.intersection(set(json.load(open(cenz_json_path,'r', encoding='utf-8')))):
        await message.reply('Привет, дорогой друг! Мат здесь запрещен.')
        await message.delete()
    else:
        city = message.text.strip().lower()
        res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
        if res.status_code == 200:
            data = json.loads(res.text)
            temp = data["main"]["temp"]
            response_message = f'Сейчас погода: {temp}'
            await bot.send_message(message.from_user.id,response_message)
        else:
            response_message = await get_negative_command_description('get_weather')
            await bot.send_message(message.from_user.id, response_message)
    await insert_data(message.from_user.id, message.from_user.full_name, message.text)
    await insert_data(message.from_user.id, message.from_user.full_name, response_message)

# Определение функции для получения новостей
async def get_news(message: types.Message):
    try:
        response_message = get_fresh_news()
        print(response_message)
        await bot.send_message(message.from_user.id, response_message[:4000])
        await insert_data(message.from_user.id, message.from_user.full_name, message.text)
        await insert_data(message.from_user.id, message.from_user.full_name, response_message)
    except:
        response_message = await get_negative_command_description('get_news')

# Определение функции для вставки данных в базу данных
@sync_to_async
def insert_data(user_id, user_name, user_message):
    print(user_id, user_name, user_message)
    try:
        existing_user = Account.objects.filter(user_num=user_id).first()
        if existing_user:
            existing_user.user_name = user_name
            existing_user.save()
            if user_message:
                now = datetime.now()
                Chat.objects.create(account=existing_user, message=user_message, time_chat=now)
        else:
            new_user = Account(user_num=user_id, user_name=user_name)
            new_user.save()
            if user_message:
                now = datetime.now()
                Chat.objects.create(account=new_user,message=user_message, time_chat=now)
    except Exception as e:
        print(e)

# Определение функции для регистрации обработчиков сообщений
def register_handler(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=[Command.objects.get(name='command_start').keyword])
    dp.register_message_handler(command_help, commands=[Command.objects.get(name='command_help').keyword])
    dp.register_message_handler(get_weather, commands=[Command.objects.get(name='get_weather').keyword])
    dp.register_message_handler(get_news, commands=[Command.objects.get(name='get_news').keyword])
    dp.register_message_handler(answer_weather)

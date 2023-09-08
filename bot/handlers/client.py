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


# @dp.message_handler(commands=['start'])

@sync_to_async
def get_command_description(command_name):
    try:
        return Command.objects.get(name=command_name).description
    except Command.DoesNotExist:
        return None
async def command_start(message: types.Message):
    try:
        response_message = await get_command_description('command_start')
        await bot.send_message(message.from_user.id,
                               response_message, reply_markup=kb_client)
        # await message.delete()
    except:
        response_message = 'Обратитесь к боту в ЛС: /n здесь дб ссылка'
        await message.reply(message.from_user.id, response_message, reply_markup=kb_client)
    await insert_data(message.from_user.id, message.from_user.full_name, message.text)
    await insert_data(message.from_user.id, message.from_user.full_name, response_message)

# @dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    try:
        response_message = await get_command_description('command_help')
        await bot.send_message(message.from_user.id, response_message)
        # print(message.from_user.id, message.from_user.last_name, message.text)
        # print(type(message.from_user.id))
        await insert_data(message.from_user.id, message.from_user.full_name, message.text)
        await insert_data(message.from_user.id, message.from_user.full_name, response_message)
    except:
        pass

async def get_weather(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пожалуйста, введите город')
    await insert_data(message.from_user.id, message.from_user.full_name, message.text)
async def answer_weather(message: types.Message):
    cenz_json_path = os.path.join(BASE_DIR, 'bot', 'cenz.json')
    if {x.lower().translate(str.maketrans('', '', string.punctuation)) for x in message.text.split(' ')}.intersection(set(json.load(open(cenz_json_path,'r', encoding='utf-8')))):
        await message.reply('Привет, дорогой друг!Мат здесь запрещен.')
        await message.delete()
    else:
        city = message.text.strip().lower()
        res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
        if res.status_code == 200:
            data = json.loads(res.text)
            temp = data["main"]["temp"]
            response_message = f'Сейчас погода: {temp}'
            await bot.send_message(message.from_user.id,response_message)
            # image = 'sunny.png' if temp > 5.0 else 'sun.png'
            # file = open('./' + image, 'rb')
            # bot.send_photo(message.chat.id, file)

        else:
            response_message = 'Эх, такой город еще не создан в 21 веке'
            await bot.send_message(message.from_user.id, response_message)

    await insert_data(message.from_user.id, message.from_user.full_name, message.text)
    await insert_data(message.from_user.id, message.from_user.full_name, response_message)

async def get_news(message: types.Message):
    response_message = get_fresh_news()
    await bot.send_message(message.from_user.id, response_message[:4000])
    await insert_data(message.from_user.id, message.from_user.full_name, message.text)
    await insert_data(message.from_user.id, message.from_user.full_name, response_message)

@sync_to_async
def insert_data(user_id, user_name, user_message):
    print(user_id, user_name, user_message)

    try:
        # Попытка найти существующего пользователя по user_id
        existing_user = Account.objects.filter(user_num=user_id).first()

        # Если пользователь существует, обновляем его имя
        if existing_user:
            existing_user.user_name = user_name
            existing_user.save()
            if user_message:
                now = datetime.now()
                # Создаем запись в чате
                Chat.objects.create(account=existing_user, message=user_message, time_chat=now)
        else:
            # Если пользователя нет, создаем нового
            new_user = Account(user_num=user_id, user_name=user_name)
            new_user.save()
            if user_message:
                now = datetime.now()
                # Создаем запись в чате
                Chat.objects.create(account=new_user,message=user_message, time_chat=now)


    #         # Здесь вы должны получить или создать аккаунт пользователя
    #         user_account, created = account.objects.get_or_create(user_num=user_id, defaults={'user_name': user_name})
    #         # Создаем запись в чате и связываем ее с аккаунтом
    #         chat.objects.create(message=user_message, time_chat=now, acc=user_account)
    except Exception as e :
        print(e)
def register_handler(dp: Dispatcher):
    dp.register_message_handler(command_start,commands=[Command.objects.get(name='command_start').keyword])
    dp.register_message_handler(command_help,commands=[Command.objects.get(name='command_help').keyword])
    dp.register_message_handler(get_weather,commands=[Command.objects.get(name='get_weather').keyword])
    dp.register_message_handler(get_news, commands=[Command.objects.get(name='get_news').keyword])
    dp.register_message_handler(answer_weather)

from aiogram import Bot, Dispatcher  # улавливает события в чате

from my_project.settings import api, token

bot = Bot(token)
dp = Dispatcher(bot)
API = api


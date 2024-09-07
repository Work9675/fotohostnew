import asyncio
from typing import List, Union
import requests
import os

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

#################################################
BOT_TOKEN = "TOKEN"##############################
#################################################

api_url = 'https://anh.moe/api/1/upload/?key=chv_MOz0_6f61ba590cd350075aa6d3c8e9576fcc49a2b420e8c817bc234ead0d739aaa4b8454ff063f92daef72717a27887a5ea242587c5ea3199e7c0cc92210c5ccb086&format=json'

re = "\033[1;31m"
gr = "\033[1;32m"
cy="\033[1;36m"

logo = (
            f"                    _             __         {re}___       __{cy}\n"
            f"               ____(_)______ ____/ /__ _____{re}/ _ )___  / /_{cy}\n"
            f"              / __/ / __/ _ `/ _  / _ `/___{re}/ _  / _ \/ __/{cy}\n"
            f"              \__/_/\__/\_,_/\_,_/\_,_/   {re}/____/\___/\__/{cy}\n"
            f"              ----------Telegram-Bot-Cicada3301-----------\n\n"
)
re = "\033[1;31m"
gr = "\033[1;32m"
cy = "\033[1;36m"


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

MethodGetMe = (f'''https://api.telegram.org/bot{BOT_TOKEN}/GetMe''')
response = requests.post(MethodGetMe)
tttm = response.json()
tk = tttm['ok']
if tk == True:
    id_us = (tttm['result']['id'])
    first_name = (tttm['result']['first_name'])
    username = (tttm['result']['username'])
    os.system('cls')
    print(logo)

    print(f"""
                ---------------------------------
                🆔 Bot id: {id_us}
                ---------------------------------
                👤 Имя Бота: {first_name}
                ---------------------------------
                🗣 username: @{username}
                ---------------------------------
                🌐 https://t.me/{username}
                ---------------------------------
                ******* Suport: @Satanasat ******
    """)
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def handle_photo(message: types.Message):
    URI_INFO = f"https://api.telegram.org/bot{BOT_TOKEN}/getFile?file_id="
    URI = f"https://api.telegram.org/file/bot{BOT_TOKEN}/"
    photo = message.photo[-1].file_id
    resp = requests.get(URI_INFO + photo)
    img_path = resp.json() ['result'] ['file_path']
    img = requests.get(URI+img_path)
    pr = img.content
    text = message.caption
    uu = []
    while True:
        try:
            data= {"expiration": "P1Y"}
            files={'source': pr}
            response = requests.post(api_url, files=files, data=data)
            data = response.json()
            print(data)
            photo_url = data["image"]["url"]
        
            uu.append(f"{photo_url}\n")
            

                
            break
        except:
            pass
    b = ''.join(uu)


    await message.reply(
                    f'Фото Загруженно: \n{b}',
                    disable_web_page_preview=True,
                )

 

if __name__ == '__main__':  
    executor.start_polling(dp, skip_updates=True)

import os 

from configs import *
from pyrogram import Client

plugins = dict(root='plugins')

bot = Client(
    "Ecuplot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    lang_code='es',
    plugins=plugins
)

if __name__ == '__main__':
    os.system('cls')
    print("Bot en linea.")
    bot.run()
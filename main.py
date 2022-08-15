import logging
import sqlite3

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


API_TOKEN = '5282687995:AAHfuJrWeGdQ-enFRLUzsy7YzCi3gJRaffc'
ADMIN_ID = 357277790

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
# bot._connector_init['ssl'] = False
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
# kb.add(types.InlineKeyboardButton(text="О боте"))
# kb.add(types.InlineKeyboardButton(text="Об авторе"))
# kb.add(types.InlineKeyboardButton(text="Контакты"))
# kb.add(types.InlineKeyboardButton(text="Будущие апдейты"))

conn = sqlite3.connect('NickLyubot_db.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(user_id INTEGER, user_name STRING, start INTEGER, about_bot INTEGER, 
            about_author INTEGER, contacts INTEGER, future INTEGER);""")
conn.commit()



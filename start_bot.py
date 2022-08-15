from aiogram import executor
from main import dp

from handlers.about_author_handler import about_author_start, about_author
from handlers.commands_base import send_welcome
from handlers.start_cbq_handler import start_cbq

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

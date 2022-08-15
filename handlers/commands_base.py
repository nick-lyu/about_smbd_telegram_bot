from aiogram import types

from main import dp, conn

from texts.texts import text_about_author, text_contacts, text_about_bot, text_future, text_start


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    print('ID:', message.from_user.id, 'NAME:', message.from_user.username, 'LNAME:', message.from_user.last_name)
    print('CHAT ID:', message.chat.id, message.chat.username, message.chat.last_name)
    # cur = conn.cursor()
    # cur.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
    # result = cur.fetchone()
    # Создать если нет и во все поля добавить ноль кроме старта, туда единицу
    # Подумать можно ли написать функцию для автоматизации всего этого
    # cur.execute(f"UPDATE users SET start = start + 1 WHERE id = {message.chat.id}")
    # conn.commit()

    keyboard = types.InlineKeyboardMarkup(row_width=1, inline_keyboard=True)
    keyboard.add(types.InlineKeyboardButton(f'Спасибо, понятно. ' + b"\xF0\x9F\x98\x8C".decode('utf-8'), callback_data='start'))
    await message.answer(text_start, reply_markup=keyboard)


"""
@dp.message_handler(commands=['about_author'])
async def about_author(message: types.Message):
    # list_about_a = text_about_author.split('\n')
    await message.answer(text_about_author)
"""


@dp.message_handler(commands=['contacts'])
async def contacts(message: types.Message):
    await message.answer(text_contacts)


@dp.message_handler(commands=['about'])
async def about(message: types.Message):
    await message.answer(text_about_bot)


@dp.message_handler(commands=['future'])
async def future(message: types.Message):
    await message.answer(text_future)

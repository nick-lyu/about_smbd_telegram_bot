from aiogram.types import CallbackQuery

from main import dp


@dp.callback_query_handler(text='start', state='*')
async def start_cbq(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.delete_reply_markup()

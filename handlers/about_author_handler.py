from aiogram import types
from aiogram.dispatcher import FSMContext

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.about_author_kb import aa_kb_maker
from main import dp
from states.about_author_state import AboutAuthor
from texts.texts import text_about_author


@dp.message_handler(Command("about_author"))
async def about_author_start(message: Message):
    await message.answer(text=text_about_author[0], reply_markup=aa_kb_maker(0))
    # await AboutAuthor.Step1.set()
    await AboutAuthor.first()

'''
@dp.callback_query_handler(text_contains='aa', state='*',)
async def about_author(call: CallbackQuery):
    await call.answer(cache_time=60)
    # await call.message.delete_reply_markup()
    n = int(call.data.split(':')[1])
    if n == len(text_about_author):
        await call.message.answer(text="Теперь вы знаете больше обо мне. Вот вам тортик " + b'\xF0\x9F\x8D\xB0'.decode('utf8'))
    else:
        await call.message.answer(text=text_about_author[n], reply_markup=aa_kb_maker(n))
    await call.message.delete_reply_markup()
'''

# @dp.message_handler(state=AboutAuthor)
# async def about_author_2(message: types.Message, state: FSMContext):
#     pass


@dp.callback_query_handler(state=AboutAuthor,) #2
async def about_author(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    print(await state.get_data())
    print(await AboutAuthor.last())
    if await state.get_state() == await AboutAuthor.last():
        print('LAST')
        await state.finish()
        await call.message.answer(text="Теперь вы знаете больше обо мне. Вот вам тортик " + b'\xF0\x9F\x8D\xB0'.decode('utf8'))
    else:
        print('CHOISE')
        a = str(await state.get_state())
        await call.message.answer(text=a, reply_markup=aa_kb_maker(0))
        await AboutAuthor.next()
        await call.message.delete_reply_markup()

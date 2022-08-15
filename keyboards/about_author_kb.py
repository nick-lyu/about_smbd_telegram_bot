from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

# kb = ReplyKeyboardMarkup(resize_keyboard=True)
from texts.keyboard_texts import about_author_kb_text


'''
aa_kb_0 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='П-нятненько... (1)', callback_data='aa:1')
        ]
    ]
)
'''


def aa_kb_maker(n):
    aa_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=about_author_kb_text[n], callback_data=f'aa:{n+1}')
            ]
        ]
    )
    return aa_kb

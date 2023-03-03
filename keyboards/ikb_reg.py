from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebhookInfo
from aiogram.utils.callback_data import CallbackData
from data.groups import magaz_cb
from data.groups import category

inline_kb_choice = InlineKeyboardMarkup(1)
btn1 = InlineKeyboardButton('Ищу работу', callback_data=magaz_cb.new(id='Worker', action='choice', order_id='-'))
btn2 = InlineKeyboardButton('Работодатель', callback_data=magaz_cb.new(id='Employer', action='choice', order_id='-'))
inline_kb_choice.add(btn1, btn2)


async def get_categories_btn():
    inline_kb_category = InlineKeyboardMarkup(1)
    for i in range(len(category)):
        btn = InlineKeyboardButton(category[i], callback_data=magaz_cb.new(id=str(i), action='category', order_id='-'))
        inline_kb_category.add(btn)
    return inline_kb_category

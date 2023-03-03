from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebhookInfo
from aiogram.utils.callback_data import CallbackData
from data.groups import magaz_cb
from data.groups import category


async def get_categories_btn():
    inline_kb_category = InlineKeyboardMarkup(1)
    for i in range(len(category)):
        btn = InlineKeyboardButton(category[i], callback_data=magaz_cb.new(id=str(i), action='cat_em', order_id='-'))
        inline_kb_category.add(btn)
    return inline_kb_category


async def get_categories_btn2():
    inline_kb_category = InlineKeyboardMarkup(1)
    for i in range(len(category)):
        btn = InlineKeyboardButton(category[i], callback_data=magaz_cb.new(id=str(i), action='cat_em2', order_id='-'))
        inline_kb_category.add(btn)
    return inline_kb_category
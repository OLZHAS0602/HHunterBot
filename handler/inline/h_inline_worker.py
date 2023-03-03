from loader import dp, bot
import typing
from aiogram import executor, md, types
from aiogram.dispatcher import FSMContext
from data.groups import magaz_cb
from state.s_reg import registr
from data.groups import category
from function.f_users import get_employer, send_msg_emp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@dp.callback_query_handler(magaz_cb.filter(action='vac_wr'))
async def query_view(query: types.CallbackQuery, callback_data: typing.Dict[str, str], state=FSMContext):
    emp_id = callback_data['id']
    msg = await get_employer(emp_id)
    inline_kb_back = InlineKeyboardMarkup(1)
    inline_kb_back.add(InlineKeyboardButton('Откликнутся',
                                            callback_data=magaz_cb.new(id=emp_id,
                                                                       action='respond', order_id='-')))
    if msg != False:
        await query.message.edit_text(msg, reply_markup=inline_kb_back)


@dp.callback_query_handler(magaz_cb.filter(action='respond'))
async def query_view(query: types.CallbackQuery, callback_data: typing.Dict[str, str], state=FSMContext):
    emp_id = callback_data['id']
    msg = await send_msg_emp(query.message.chat.id, emp_id)

    if msg != False:
        await query.message.edit_text("Ваше обращение было выслана работодател, теперь ждите ответа")
        #await query.message.edit_text(msg, reply_markup=inline_kb_back)

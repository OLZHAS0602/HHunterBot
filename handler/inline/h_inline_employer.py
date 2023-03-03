from loader import dp, bot
import typing
from aiogram import executor, md, types
from aiogram.dispatcher import FSMContext
from data.groups import magaz_cb
from state.s_reg import registr
from data.groups import category
from function.f_users import get_user_by_vac, get_user_questionnaire, get_user
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from state.s_add_vac import Vacancies


@dp.callback_query_handler(magaz_cb.filter(action='cat_em'), state="*")
async def query_view(query: types.CallbackQuery, callback_data: typing.Dict[str, str], state=FSMContext):
    id = callback_data['id']
    vac = category[int(id)]
    await get_user_by_vac(vac, query.message.chat.id)


@dp.callback_query_handler(magaz_cb.filter(action='questionnaire'), state="*")
async def query_view(query: types.CallbackQuery, callback_data: typing.Dict[str, str], state=FSMContext):
    workerID = callback_data['id']
    msg = await get_user_questionnaire(workerID, query.message.chat.id)
    #inline_kb_back = InlineKeyboardMarkup(1)
    #inline_kb_back.add(InlineKeyboardButton('Назад',
    #                                       callback_data=magaz_cb.new(id=workerID,
    #                                                                  action='back_quest', order_id='-')))
    if msg != False:
        await query.message.edit_text(msg)


@dp.callback_query_handler(magaz_cb.filter(action='cat_em2'), state=Vacancies.waiting_vac)
async def query_view(query: types.CallbackQuery, callback_data: typing.Dict[str, str], state=FSMContext):
    id = callback_data['id']
    vac = category[int(id)]
    await state.update_data(vacancies=vac)
    await query.message.edit_text("Напишиште сколько лет стажа нужно для этой работы")
    await Vacancies.waiting_exp.set()



#@dp.callback_query_handler(magaz_cb.filter(action='back_quest'), state="*")
#async def query_view(query: types.CallbackQuery, callback_data: typing.Dict[str, str], state=FSMContext):
#    id = callback_data['id']
#    msg = await get_user_questionnaire(id, query.message.chat.id)
from loader import dp, bot
import typing
from aiogram import executor, md, types
from aiogram.dispatcher import FSMContext
from data.groups import magaz_cb
from state.s_reg import registr
from data.groups import category


@dp.callback_query_handler(magaz_cb.filter(action='choice', id='Worker'), state=registr.waiting_choice)
async def query_view(query: types.CallbackQuery, callback_data: typing.Dict[str, str], state=FSMContext):
    msg = await query.message.edit_text("Напишите email, что бы связаться с вами")
    await state.update_data(lvl=msg)
    await state.update_data(choice="worker")
    await registr.waiting_email_wr.set()


@dp.callback_query_handler(magaz_cb.filter(action='choice', id='Employer'), state=registr.waiting_choice)
async def query_view(query: types.CallbackQuery, callback_data: typing.Dict[str, str], state=FSMContext):
    msg = await query.message.edit_text("Напишите email, что бы связаться с вами")
    await state.update_data(lvl=msg)
    await state.update_data(choice="employer")
    await registr.waiting_email_em.set()


@dp.callback_query_handler(magaz_cb.filter(action='category'), state=registr.waiting_prefer_vac_wr)
async def query_view(query: types.CallbackQuery, callback_data: typing.Dict[str, str], state=FSMContext):
    id = callback_data['id']
    msg = await query.message.edit_text("Напишите стаж работы(Сколько лет вы отроботали на этой вакансий)")
    await state.update_data(lvl=msg)
    name = category[int(id)]
    await state.update_data(category=name)
    await registr.waiting_experience_wr.set()


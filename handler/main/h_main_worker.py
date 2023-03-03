from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType
from aiogram.dispatcher.filters import Text
from keyboards.ikb_employer import get_categories_btn
from state.s_add_vac import Vacancies
from function.f_users import get_vacancies_for_worker



@dp.message_handler(Text(equals="Поиск вакансий"), state="*")
async def main_employer(message: types.Message, state=FSMContext):
    if await get_vacancies_for_worker(message.chat.id) == False:
        await message.answer("Вакансий пока нет")
    #await message.answer("", reply_markup=await get_categories_btn())
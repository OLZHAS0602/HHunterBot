from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType
from aiogram.dispatcher.filters import Text
from keyboards.ikb_employer import get_categories_btn, get_categories_btn2
from state.s_add_vac import Vacancies
from function.f_users import add_vacancies


@dp.message_handler(Text(equals="Поиск сотрудников"), state="*")
async def main_employer(message: types.Message, state=FSMContext):
    await message.answer("Выберите вакансию", reply_markup=await get_categories_btn())


@dp.message_handler(Text(equals="Добавить вакансию"), state="*")
async def main_employer(message: types.Message, state=FSMContext):
    await message.answer("Выберите вакансию", reply_markup=await get_categories_btn2())
    await Vacancies.waiting_vac.set()


@dp.message_handler(state=Vacancies.waiting_exp)
async def main_employer(message: types.Message, state=FSMContext):
    try:
        int(message.text)
        await state.update_data(exp=message.text)
        await message.answer("Напишите о работе, что он должен делать на этой должности и какими навыками он должен овладать")
        await Vacancies.waiting_about.set()
    except Exception as ex:
        await message.answer(
            "Ввдеите число")
        print(ex)


@dp.message_handler(state=Vacancies.waiting_about)
async def main_employer(message: types.Message, state=FSMContext):
    data = await state.get_data()
    if await add_vacancies(message.chat.id, data['vacancies'], data['exp'], str(message.text)):
        await message.answer("Вы добавили вакансию")
    else:
        await message.answer("Пройзашла ошибка")

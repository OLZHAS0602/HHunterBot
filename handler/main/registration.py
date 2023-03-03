from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType
from aiogram.dispatcher.filters import Text
from function.f_users import check_users
from keyboards.kb_employer import employer_main
from keyboards.kb_worker import worker_main
from state.s_reg import registr
from keyboards.ikb_reg import inline_kb_choice
from keyboards.ikb_reg import get_categories_btn
from function.f_users import add_employer, add_workers, get_name


@dp.message_handler(content_types=ContentType.CONTACT)
async def reg(message: types.Message, state=FSMContext):
#    print("TEst")
    phone_number = message.contact.phone_number
    name = await check_users(message.from_user.id)
    if name != False:

        if name == "Employers":
            fio = await get_name(name, message.chat.id, 1)
            kb = employer_main
        elif name == "Workers":
            fio = await get_name(name, message.chat.id, 2)
            kb = worker_main
        await message.answer("Добро пожаловать, " + fio, reply_markup=kb)
    else:
        await state.update_data(user_phone=phone_number)
        await state.update_data(tlgID=message.from_user.id)
        #await message.answer("Мы не нашли вас в базе. Что бы учавствовать в розыгрыше вам необходимо зарегистрироваться")
        msg = await message.answer("Введите ваше ФИО")
        await state.update_data(lvl=msg)
        await registr.waiting_FIO.set()


@dp.message_handler(state=registr.waiting_FIO)
async def reg(message: types.Message, state=FSMContext):
    data = await state.get_data()
    msg = data['lvl']
    await state.update_data(FIO=message.text)
    await bot.delete_message(message.chat.id, message.message_id)
    await msg.edit_text("Вы ищете работу или вы частный работодатель?", reply_markup=inline_kb_choice)
    await registr.waiting_choice.set()


@dp.message_handler(state=registr.waiting_email_wr)
async def reg(message: types.Message, state=FSMContext):
    data = await state.get_data()
    msg = data['lvl']
    await state.update_data(email=message.text)
    await bot.delete_message(message.chat.id, message.message_id)
    msg = await msg.edit_text("Пожалуйста укажите ваш адресс проживания")
    await state.update_data(lvl=msg)
    await registr.waiting_address_wr.set()


@dp.message_handler(state=registr.waiting_email_em)
async def reg(message: types.Message, state=FSMContext):
    data = await state.get_data()
    msg = data['lvl']
    await state.update_data(email=message.text)
    await bot.delete_message(message.chat.id, message.message_id)
    msg = await msg.edit_text("Пожалуйста укажите ваш адресс проживания")
    await state.update_data(lvl=msg)
    await registr.waiting_address_em.set()


@dp.message_handler(state=registr.waiting_address_wr)
async def reg(message: types.Message, state=FSMContext):
    data = await state.get_data()
    msg = data['lvl']
    await state.update_data(address=message.text)
    await bot.delete_message(message.chat.id, message.message_id)
    await msg.edit_text("Выберите предпочитаемую вакансию", reply_markup=await get_categories_btn())
    await registr.waiting_prefer_vac_wr.set()


@dp.message_handler(state=registr.waiting_experience_wr)
async def reg(message: types.Message, state=FSMContext):
    data = await state.get_data()
    msg = data['lvl']
    try:
        int(message.text)
        await state.update_data(experience=message.text)
        await bot.delete_message(message.chat.id, message.message_id)
        msg = await msg.edit_text("Напишите в что вы делали и в каких компаниях вы работали(Коротка)")
        await state.update_data(lvl=msg)
        await registr.waiting_about_work_wr.set()
    except Exception as ex:
        await msg.edit_text("Введите число")
        await registr.waiting_experience_wr.set()
        print(ex)


@dp.message_handler(state=registr.waiting_about_work_wr)
async def reg(message: types.Message, state=FSMContext):
    data = await state.get_data()
    msg = data['lvl']
    about_work = str(message.text)
    await bot.delete_message(message.chat.id, message.message_id)

    if await add_workers(data['tlgID'], data['user_phone'], data['FIO'], data['email'], data['address'], data['category'], data['experience'], about_work):
        await message.answer("Добро пожаловать", reply_markup=worker_main)
        #await msg.edit_text("Добро пожаловать", reply_markup=worker_main)
    else:
        await msg.edit_text("Пройзошла ошибка")
    await state.finish()

@dp.message_handler(state=registr.waiting_address_em)
async def reg(message: types.Message, state=FSMContext):
    data = await state.get_data()
    msg = data['lvl']
    await state.update_data(address=message.text)
    await bot.delete_message(message.chat.id, message.message_id)
    msg = await msg.edit_text("Введите название компаний")
    await state.update_data(lvl=msg)
    await registr.waiting_company_name_em.set()


@dp.message_handler(state=registr.waiting_company_name_em)
async def reg(message: types.Message, state=FSMContext):
    data = await state.get_data()
    msg = data['lvl']
    await state.update_data(company_name=message.text)
    await bot.delete_message(message.chat.id, message.message_id)
    msg = await msg.edit_text("Напишите о вашей компаний(на чем специализируется и т.д.)")
    await state.update_data(lvl=msg)
    await registr.waiting_about_company_em.set()


@dp.message_handler(state=registr.waiting_about_company_em)
async def reg(message: types.Message, state=FSMContext):
    data = await state.get_data()
    msg = data['lvl']
    about_company = str(message.text)
    #await state.update_data(email=message.text)
    await bot.delete_message(message.chat.id, message.message_id)
    if await add_employer(data['tlgID'], data['user_phone'], data['FIO'], data['email'], data['address'], data['company_name'], about_company):
        #await msg.edit_text("Добро пожаловать", reply_markup=employer_main)
        await message.answer("Добро пожаловать", reply_markup=employer_main)
    else:
        await msg.edit_text("Пройзошла ошибка")
    await state.finish()

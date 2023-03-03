from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from aiogram.dispatcher import FSMContext
from keyboards.kb_worker import phonemarkup


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Добрый день, вас приветствует бот "
                         "что бы продолжить дальше, нажмите кнопку ниже "
                         "и подилитесь номером телефона", reply_markup=phonemarkup)

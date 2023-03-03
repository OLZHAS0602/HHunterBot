from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class registr(StatesGroup):
    waiting_FIO = State()
    waiting_choice = State()
    #Стейты для Workers
    waiting_email_wr = State()
    waiting_address_wr = State()
    waiting_prefer_vac_wr = State()
    waiting_experience_wr = State()
    waiting_about_work_wr = State()
    #Стейты для Emolyers
    waiting_email_em = State()
    waiting_address_em = State()
    waiting_company_name_em = State()
    waiting_about_company_em = State()

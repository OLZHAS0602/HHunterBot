from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class Vacancies(StatesGroup):
    waiting_vac = State()
    waiting_exp = State()
    waiting_about = State()
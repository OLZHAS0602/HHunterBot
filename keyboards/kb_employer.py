from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

employer_main = ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
btn1 = KeyboardButton('Поиск сотрудников')
btn2 = KeyboardButton('Добавить вакансию')
#btn3 = KeyboardButton('Личный кабинет')
employer_main.add(btn1)
employer_main.add(btn2)
#employer_main.add(btn3)
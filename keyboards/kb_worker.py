from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phonemarkup = ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
btn1 = KeyboardButton('Поделиться номером', request_contact=True)
phonemarkup.add(btn1)
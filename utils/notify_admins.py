import logging

from aiogram import Dispatcher
from data.groups import groups


async def on_startup_notify(dp: Dispatcher):
        try:
            for key in groups:
                if groups[key] == "admin":
                    await dp.bot.send_message(key, "Бот запущен")
            print(await dp.bot.get_webhook_info())
        except Exception as err:
            logging.exception(err)

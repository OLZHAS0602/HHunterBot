from aiogram import executor

from loader import dp, on_shutdown
from utils.notify_admins import on_startup_notify
from schedule_works import on_startup
import middlewares, handler

#async def on_startup(dispatcher):
    # Уведомляет про запуск
#    await on_startup_notify(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown())

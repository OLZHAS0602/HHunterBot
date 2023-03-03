from loader import dp,  bot
from utils.notify_admins import on_startup_notify
from function.f_users import init

async def on_startup(dispatcher):
    # Уведомляет про запуск
    await init()
    await on_startup_notify(dispatcher)




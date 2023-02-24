import asyncio

from aiogram import executor

from data.config import BOT_TOKEN, WEBHOOK_HOST, WEBAPP_PORT
from loader import dp, on_shutdown, bot
import middlewares, handler
from utils.notify_admins import on_startup_notify
from aiogram.utils.executor import start_webhook
from schedule_works import on_startup




WEBHOOK_PATH = f'/{BOT_TOKEN}'
WEBHOOK_URL =f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = '0.0.0.0'  # or ip


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )

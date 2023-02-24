from aiogram import executor

from loader import dp, on_shutdown, bot
import middlewares, handler
from utils.notify_admins import on_startup_notify
from aiogram.utils.executor import start_webhook

from pyngrok import ngrok

http_tunnel = ngrok.connect()
tunnel = ngrok.get_tunnels()[0].public_url


async def on_startup(dispatcher):
    # Уведомляет про запуск
    await bot.set_webhook(WEBHOOK_URL)
    await on_startup_notify(dispatcher)


WEBHOOK_PATH = ''
WEBHOOK_URL = f"{tunnel}"

# webserver settings
WEBAPP_HOST = '127.0.0.1'  # or ip
WEBAPP_PORT = 80

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

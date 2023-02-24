from loader import dp,  bot
from utils.notify_admins import on_startup_notify
import datetime
import aioschedule as schedule
import asyncio
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from requests.structures import CaseInsensitiveDict
from base64 import b64encode
import json
import requests
from function.f_connectsql import connection
from function.f_val import is_older18
from data.config import BOT_TOKEN, WEBHOOK_HOST, WEBAPP_PORT
#from function.f_user import del_chek_user

async def on_startup(dispatcher):
    # Уведомляет про запуск
    WEBAPP_HOST = '0.0.0.0'
    WEBHOOK_PATH = f'/{BOT_TOKEN}'
    WEBHOOK_URL =f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
    await bot.set_webhook(WEBHOOK_URL)
    asyncio.create_task(scheduler())
    await on_startup_notify(dispatcher)

async def scheduler():
    #schedule.every(30).minute.do(birthday())
    #schedule.every().days.at("10:00").do(birthday)
    loop = asyncio.get_event_loop()
    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)

async def birthday():
    conn = await connection()
    cursor = conn.cursor()
    sql = "SELECT userID FROM users_KinderClub;"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            userID = str(row[0])
            sql2 = "SELECT * FROM children_KinderClub WHERE user_id = '" + str(userID) + "';"
            cursor.execute(sql2)
            result2 = cursor.fetchall()
            for row2 in result2:
                ID = str(row2[0])
                FIO = str(row2[1])
                Date = str(row2[2])
                year = datetime.datetime.now().year
                day = datetime.datetime.now().day
                month = datetime.datetime.now().month
                #now_date = datetime.date(year = year,day=day,month=month)

                s = str(Date).split('.')
                birth_date = datetime.date(year=int(s[2]), day=int(s[0]) - 5, month=int(s[1])).strftime('%d.%m.%Y')
                res = is_older18(Date)
                res2 = is_older18(str(birth_date))
                if res:
                    if month == int(s[1]) and int(s[0]) - int(day) == 5 and res2 != 'older':
                        await bot.send_message(userID, "У вашего ребенка(" + FIO + ") через 5 дней день "
                                                      "рождения, постите наш магазин и "
                                                      "мы вам дадим скидку")
                    elif month == int(s[1]) and int(s[0]) == int(day):
                        await bot.send_message(userID, "С днем рождения " + FIO + " приходите к нам и мы дадим вам скидку на любой товар")

                #birth_date = datetime.date(year = int(s[2]),day = int(s[0]),month = int(s[1]))
    except Exception as ex:
        print(ex)
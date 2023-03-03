from function.f_connectsql import connection
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import dp, bot
from data.groups import magaz_cb


async def init():
    conn = await connection()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Employers(
            EmployerId INT PRIMARY KEY,
            FIO TEXT,
            tlg_id TEXT,
            Name_company TEXT,
            Number TEXT,
            Mail TEXT,
            Address TEXT,
            About_company TEXT);
            """)

    cur.execute("""CREATE TABLE IF NOT EXISTS Workers(
            WorkerId INT PRIMARY KEY,
            tlg_id TEXT,
            FIO TEXT,
            Number TEXT,
            Mail TEXT,
            Address TEXT,
            Pref_vacation TEXT,
            Experience TEXT,
            About_work TEXT);
            """)

    cur.execute("""CREATE TABLE IF NOT EXISTS Vacancies(
            VacanciesId INT PRIMARY KEY,
            EmployerId TEXT,
            VacanciesName TEXT,
            Experience TEXT,
            About_work TEXT);
            """)
    conn.commit()
    conn.close()


async def add_vacancies(tlg_id, vac, exp, ab_work):
    conn = await connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT into Vacancies(EmployerId, VacanciesName, Experience, About_work) "
                    "VALUES(?, ?, ?, ?)", (tlg_id, vac, exp, ab_work))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        return False


async def check_users(user_id: str):
    conn = await connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Employers WHERE tlg_id = '" + str(user_id) + "';")
    result = cur.fetchone()
    if result:
        conn.commit()
        conn.close()
        return "Employers"
    cur.execute("SELECT * FROM Workers WHERE tlg_id = '" + str(user_id) + "';")
    result = cur.fetchone()
    if result:
        conn.commit()
        conn.close()
        return "Workers"
    else:
        return False


async def add_employer(tlg_id, phone, fio, mail, address, company_name, about_company):
    conn = await connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT into Employers(tlg_id, Name_company, FIO, Number, Mail, Address, About_company) "
                    "VALUES(?, ?, ?, ?, ?, ?, ?)",
                    (str(tlg_id), str(company_name), str(fio), str(phone), str(mail), str(address), str(about_company)))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False


async def add_workers(tlg_id, phone, fio, mail, address, prefer_vacation, experience, about_work):
    conn = await connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT into Workers(tlg_id, FIO, Number, Mail, Address, Pref_vacation, Experience, About_work) "
                    "VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                    (str(tlg_id), str(fio), str(phone), str(mail), str(address), str(prefer_vacation), str(experience), str(about_work)))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False


async def get_name(name, tlg_id, col):
    conn = await connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM " + name + " WHERE tlg_id = '" + str(tlg_id) + "';")
        result = cur.fetchall()
        for row in result:
            fio = str(row[col])
        conn.commit()
        conn.close()
        return fio
    except Exception as ex:
        print(ex)
        return False


async def get_user_by_vac(vacation, tlg_id):
    conn = await connection()
    cur = conn.cursor()
    try:

        cur.execute("SELECT * FROM Workers WHERE Pref_vacation = '" + str(vacation) + "';")
        result = cur.fetchall()
        for row in result:
            inline_kb_fio = InlineKeyboardMarkup(1)
            worker_tlgID = str(row[1])
            fio = str(row[2])
            experience = str(row[7])
            about_work = str(row[8])
            msg = "ФИО: " + fio + "\n" + \
                  "Опыт работы: " + experience + "\n"\
                  "О работе: " + about_work
            inline_kb_fio.add(InlineKeyboardButton('Открыть',
                                                   callback_data=magaz_cb.new(id=worker_tlgID,
                                                                              action='questionnaire', order_id='-')))
            await bot.send_photo(tlg_id, "1869679.png", caption=msg, reply_markup=inline_kb_fio)

            #phone = str(row[3])
            #mail = str(row[4])
            #address = str(row[5])
            #vacation = str(row[6])

        conn.commit()
        conn.close()
    except Exception as ex:
        print(ex)

async def get_user(workerID):
    conn = await connection()
    cur = conn.cursor()
    try:
        inline_kb_fio = InlineKeyboardMarkup(1)
        cur.execute("SELECT * FROM Workers WHERE tlg_id = '" + str(workerID) + "';")
        result = cur.fetchall()
        for row in result:
            worker_tlgID = str(row[1])
            fio = str(row[2])
            experience = str(row[7])
            about_work = str(row[8])

        msg = "ФИО: " + fio + "\n" + \
              "Опыт работы: " + experience + "\n" \
              "О работе: " + about_work
        inline_kb_fio.add(InlineKeyboardButton('Открыть',
                                               callback_data=magaz_cb.new(id=worker_tlgID,
                                                                          action='questionnaire', order_id='-')))
    except Exception as ex:
        print(ex)
        #await bot.send_photo(tlg_id, "1869679.png", caption=msg, reply_markup=inline_kb_fio)



async def get_user_questionnaire(worker_tlgID, tlgID):
    conn = await connection()
    cur = conn.cursor()
    try:
        #inline_kb_back = InlineKeyboardMarkup(1)
        #inline_kb_back.add(InlineKeyboardButton('Назад',
        #                                       callback_data=magaz_cb.new(id=worker_tlgID,
        #                                                                  action='back_quest', order_id='-')))
        cur.execute("SELECT * FROM Workers WHERE tlg_id = '" + str(worker_tlgID) + "';")
        result = cur.fetchall()
        for row in result:
            phone = str(row[3])
            mail = str(row[4])
            address = str(row[5])
            vacation = str(row[6])
            msg = "Телефон: " + phone + "\n" + \
                  "Email: " + mail + "\n" + \
                  "Адресс: " + address + "\n" + \
                  "Вакансия: " + vacation + "\n"
            #await bot.send_photo(tlgID, "1869679.png", caption=msg)
        conn.commit()
        conn.close()
        return msg
    except Exception as ex:
        print(ex)
        return False


async def get_vacancies_for_worker(tlg_id):
    conn = await connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT Pref_vacation FROM Workers WHERE tlg_id = '" + str(tlg_id) + "';")
        result = cur.fetchall()
        for row in result:
            vac = str(row[0])
        cur.execute("SELECT * FROM Vacancies WHERE VacanciesName = '" + vac + "';")
        result = cur.fetchall()
        if result:
            for row in result:
                inline_kb_vac = InlineKeyboardMarkup(1)
                about_work = str(row[4])
                exp = str(row[3])
                emp_id = str(row[1])
                msg = "О работе: " + about_work + "\n"\
                      "Опыт работы: " + exp + "года"
                inline_kb_vac.add(InlineKeyboardButton('Посмотреть',
                                                       callback_data=magaz_cb.new(id=emp_id,
                                                                                  action='vac_wr', order_id='-')))
                await bot.send_message(tlg_id, msg, reply_markup=inline_kb_vac)
            conn.commit()
            conn.close()
        else:
            return False
    except Exception as ex:
        print(ex)


async def get_employer(tlg_id):
    conn = await connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM Employers WHERE tlg_id = '" + str(tlg_id) + "';")
        result = cur.fetchall()
        if result:
            for row in result:
                name_company = str(row[3])
                phone = str(row[4])
                mail = str(row[5])
                address = str(row[6])
                msg = "Название компаний: " + name_company + "\n" + \
                      "Номер телефона: " + phone + "\n" + \
                      "Email: " + mail + "\n" + \
                      "Адресс: " + address
            conn.commit()
            conn.close()
            return msg
        else:
            return False
    except Exception as ex:
        return False


async def send_msg_emp(tlg_id, emp_id):
    conn = await connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM Workers WHERE tlg_id = '" + str(tlg_id) + "';")
        result = cur.fetchall()
        if result:
            for row in result:
                phone = str(row[3])
                mail = str(row[4])
                address = str(row[5])
                vacation = str(row[6])
                fio = str(row[2])
                experience = str(row[7])
                about_work = str(row[8])
                msg = "На ваше обьявление откликнулись\nВот его анкета\n" + "ФИО: " + fio + "\n" + \
                    "Email: " + mail + "\n" + \
                    "Телефон: " + phone + "\n" + \
                    "Опыт работы: " + experience + "\n" + \
                    "О работе: " + about_work
            conn.commit()
            conn.close()
            await bot.send_message(emp_id, msg)
        else:
            return False
    except Exception as ex:
        return False
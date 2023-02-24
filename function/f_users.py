from function.f_connectsql import connection

async def init():
    conn = await connection()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Employers(
            EmployerId INT PRIMARY KEY,
            tlg_id TEXT,
            Name_company TEXT,
            Number TEXT,
            Mail TEXT,
            Adress TEXT
            About_company TEXT);
            """)

    cur.execute("""CREATE TABLE IF NOT EXISTS Workers(
            WorkerId INT PRIMARY KEY,
            tlg_id TEXT,
            FIO TEXT,
            Number TEXT,
            Mail TEXT,
            Adress TEXT,
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

async def check_users(user_id: str):
    conn = await connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Employers WHERE tlg_id = '" + user_id + "';")
    result = cur.fetchone()
    if result:
        return "Employer"
    cur.execute("SELECT * FROM Workers WHERE tlg_id = '" + user_id + "';")
    result = cur.fetchone()
    if result:
        return "Workers"
    else:
        return False


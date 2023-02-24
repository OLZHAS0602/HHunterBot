import sqlite3

async def connection():
    conn = sqlite3.connect('orders.db')
    #cur = conn.cursor()
    return conn
    #cur.execute("""CREATE TABLE IF NOT EXISTS users(
    #   userid INT PRIMARY KEY,
    #   fname TEXT,
    #   lname TEXT,
    #   gender TEXT);
    #""")
    #conn.commit()
#    try:
#        conn = pymysql.connect(
#            host="185.146.3.92",
#            port=3306,
#            user="user1",
#            password="stratton1488",
#            database="strattonkz",
#            cursorclass=pymysql.cursors.Cursor
#        )
#        return conn
#    except Exception as ex:
#        print(ex)
#        return False

#https://api.telegram.org/bot<Token>/sendMessage?chat_id=@MyUser&text=Hello
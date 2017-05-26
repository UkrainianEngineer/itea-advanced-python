# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('test_base2.sqlite')
cur = conn.cursor()

# Функция занесения пользователя в базу
def add_user(username, userpass):
    cur.execute("INSERT INTO users (name, password) VALUES ('%s', '%s')"
                %(username, userpass))
    conn.commit()

# Вводим данные
name = raw_input("Enter your name: ")
password = raw_input("Enter password: ")

# Делаем запрос в базу
print("Users list:")
add_user(name, password)
cur.execute('SELECT * FROM users')
row = cur.fetchone()

# выводим список пользователей в цикле
while row is not None:
   print("id:"+str(row[0])+"| mame: "+row[1]+" | password: "+row[2])
   row = cur.fetchone()

# закрываем соединение с базой
cur.close()
conn.close()

# -*- coding: utf-8 -*-
import sqlite3
#Подключение к базе
conn = sqlite3.connect('test_base.sqlite')
#Создание курсора
cur = conn.cursor()
#Создание таблицы
cur.execute('''CREATE TABLE users (id int auto_increment primary key,
               name varchar, password varchar)''')
#Наполнение таблицы
cur.execute("INSERT INTO users (name, password) VALUES ('admin', '123')")
#Подтверждение отправки данных в базу
conn.commit()
#Завершение соединения
cur.close()
conn.close()
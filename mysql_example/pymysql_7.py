# coding: utf-8

import pymysql

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'db': 'my_home',
    'user': 'root',
    'passwd': '123456',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

connect = pymysql.connect(**config)
cursor = connect.cursor()

cursor.execute('select * from `admin`')

# print(cursor.fetchone())
# print(cursor.fetchmany(3))
print(cursor.fetchall())
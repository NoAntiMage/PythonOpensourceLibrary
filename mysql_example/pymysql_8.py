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

with connect.cursor() as cursor:
    cursor.execute('select * from users')
    rows = cursor.fetchall()
    desc = cursor.description
    print(desc)
    # print('{0} {1}'.format(desc[0][0],desc[1][0]))
    # for row in desc:
    #     print('{0:3} {1:>10}'.format(row[0],row[2]))


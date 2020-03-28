# coding: utf-8
# reference: https://github.com/PyMySQL/PyMySQL

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
try:
    with connect.cursor() as cursor:
        sql = 'INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)'
        cursor.execute(sql,('wujiwust@gmail.com','very-secret'))

        connect.commit()

    with connect.cursor() as cursor:
        sql = 'SELECT `id`, `password` FROM `users` WHERE `email`=%s'
        cursor.execute(sql, ('wujiwust@gmail.com'))
        result = cursor.fetchone()
        print(result)
finally:
    connect.close()

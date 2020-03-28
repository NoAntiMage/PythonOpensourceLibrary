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

effect_row = cursor.execute('''
create table `admin` (
`name` varchar(32) not null,
`age` int(10) unsigned not null default '0',
primary key(`name`)
)engine=InnoDB default charset=utf8
''')

result1 = cursor.execute('insert into `admin` (`name`, `age`) values(%s, %s)',('wujimaster',18))

info = {'name': 'fake', 'age': 15}
result2 = cursor.execute('insert into `admin` (`name`, `age`) values(%(name)s, %(age)s)', info)
connect.commit()

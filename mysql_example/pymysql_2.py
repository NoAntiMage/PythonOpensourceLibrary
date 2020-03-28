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

sql = '''
create table users(
id int(5) not null AUTO_INCREMENT PRIMARY KEY,
user varchar(10) not null,
password int(20) not null
)
'''

cursor.execute(sql)


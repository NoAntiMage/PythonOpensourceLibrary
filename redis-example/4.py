# coding: UTF-8

import json
import redis
import time


def get_config():
    with open('./config.json', 'r') as f:
        content = f.read()
        redis_config = json.loads(content)
    print(redis_config)
    return redis_config


my_config = get_config()
pool = redis.ConnectionPool(**my_config)
r = redis.Redis(**my_config)

# ex - 过期时间（秒）
# px - 过期时间（毫秒）
# nx - 如果设置为True，则只有name不存在时，当前set操作才执行
# xx - 如果设置为True，则只有name存在时，当前set操作才执行

r.set('food', 'mutton', ex=3)


print r.get('food')
time.sleep(3)
print r.get('food')

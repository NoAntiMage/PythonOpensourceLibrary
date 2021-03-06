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

print r.setnx('fruit1', 'banana')
print r.setex('fruit1', 5, 'banana')


import json
import redis


def get_config():
    with open('./config.json', 'r') as f:
        content = f.read()
        redis_config = json.loads(content)
    print(redis_config)
    return redis_config


my_config = get_config()
r = redis.StrictRedis(**my_config)

r.set('foo', 'bar')
print type(r)
print r['foo']
print r.get('foo')
print type(r.get('foo'))

import json
from kazoo.client import KazooClient

with open('./config.json') as f:
    content = f.read()
    config = json.loads(content)
    # print content

zk = KazooClient(**config)
zk.stop()
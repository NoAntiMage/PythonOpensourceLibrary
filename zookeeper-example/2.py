import logging
import json
from kazoo.client import KazooClient,\
                          KazooState


def my_listener(state):
    if state == KazooState.LOST:
        print 'lost'
    elif state == KazooState.SUSPENDED:
        print 'suspended'
    else:
        print 'connected'


logging.basicConfig()

with open('./config.json') as f:
    content = f.read()
    config = json.loads(content)
    # print content

zk = KazooClient(**config)
zk.add_listener(my_listener)

zk.start()
zk.stop()

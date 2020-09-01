import logging
import json
from kazoo.client import KazooClient,\
                          KazooState,\
                          KeeperState

logging.basicConfig()

with open('./config.json') as f:
    content = f.read()
    config = json.loads(content)
    # print content

zk = KazooClient(**config)


@zk.add_listener
def watch_for_ro(state):
    if state == KeeperState.CONNECTED_RO:
        print "Read only mode!"
    else:
        print "Read/Write mode!"


zk.start()
zk.stop()



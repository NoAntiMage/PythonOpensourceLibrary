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

zk.start()
# Ensure a path, create if necessary
zk.ensure_path("/my/favorite")

# Create a node with data
zk.create("/my/favorite/node", b"a value")

# Determine if a node exists
if zk.exists("/my/favorite"):
    print "do something"

# Print the version of a node and its data
data, stat = zk.get("/my/favorite")
print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

# List the children
children = zk.get_children("/my/favorite")
print("There are %s children with names %s" % (len(children), children))

# Update value
zk.set("/my/favorite", b"some data")

# Delete node
zk.delete("/my/favorite/node", recursive=True)
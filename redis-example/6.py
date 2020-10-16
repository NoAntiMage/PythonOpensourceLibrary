from rediscluster import RedisCluster

startup_nodes = [{"host": "192.168.239.157", "port": "7002"}, {"host": "192.168.239.157", "port": "7001"}]

rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

# rc.set("foo", "bar")

print(rc.get("foo"))

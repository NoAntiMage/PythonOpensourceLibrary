import psutil, datetime
from subprocess import PIPE

# cpu
print psutil.cpu_times()
print psutil.cpu_times().user
print psutil.cpu_count()
print psutil.cpu_count(logical=False)

# mem
mem = psutil.virtual_memory()
print mem
print mem.total
print mem.free
print psutil.swap_memory()

# disk
print psutil.disk_partitions()
print psutil.disk_usage('/')

# network
print psutil.net_io_counters()

# etc
print psutil.users()
print psutil.boot_time()
print datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')

# ps
print psutil.pids()
p = psutil.Process()
print p.name()
print p.exe()
print p.cwd()
print p.status()
print p.create_time()
print p.uids()
print p.gids()
print p.cpu_times()
print p.cpu_affinity()
print p.memory_percent()
print p.memory_info()
print p.connections()
print p.num_threads()

p2 = psutil.Popen('/usr/bin/python','-c','print("hello")',stdout=PIPE)
print p2.name()
print p2.communicate()
print p2.cpu_times()


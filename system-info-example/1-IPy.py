import IPy
print IPy.IP('10.0.0.0/8').version()
print IPy.IP('::1').version()

ip = IPy.IP('192.168.0.0/16')
print ip.len()
for x in ip:
    print(x)

print ip.reverseNames()
print ip.iptype()
print ip.int()
print ip.strHex()
print ip.strBin()

print IPy.IP('192.168.1.100') < IPy.IP('12.0.0.0/24')
if '192.168.1.100' in IPy.IP('192.168.0.0/16'):
    print True

print IPy.IP('192.168.1.100').overlaps('192.168.1.10/24')


ip_s = raw_input("PLease input an IP or net-range")
ips = IPy.IP(ip_s)
if len(ips) > 1:
    print('net: %s' % ips.net())
    print('netmask: %s' % ips.netmask())
    print('broadcast: %s' % ips.broadcast())
    print('reverse address: %s' % ips.reverseNames()[0])
    print('subnet: %s ' % len(ips))
else:
    print('reverse address: %s' %ips.reverseNames()[0])

print('hexadecimal: %s' % ips.strHex())
print('binary ip: %s' % ips.strBin())
print('iptype: %s' % ips.iptype())
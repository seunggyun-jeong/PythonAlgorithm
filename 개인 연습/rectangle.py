class IP :
    def __init__(self, ip):
        self.ip = ip
        self.isUsed = 0
        self.isUsing = 0

IPs = {}
for i in range(1, 4) :
    ip = '192.168.0.%d %d' %(i,4)
    print(ip)
    IPs[ip] = IP(ip)

print(IPs['192.168.0.2'].ip)
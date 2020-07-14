import nmap


ns = nmap.PortScanner()
print(ns.nmap_version())
ns.scan('192.168.1.1', '80-631', '-v --version-all')

# print(ns.scaninfo())
# print(ns.csv())

print(ns.scanstats())
# print(ns.all_hosts())
# print(ns['192.168.1.1'].state())
# print(ns['192.168.1.1'].all_protocols())
# print(ns['192.168.1.5']['tcp'].keys())
print(ns['192.168.1.1'].has_tcp(80))
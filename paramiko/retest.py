import re
intf_ips = 'Gi0/0/0.911 10.200.101.242 YES VNRAM up   up \n'
intf_ips = intf_ips + "Gi0/0/0.900 10.200.10.200 YES VNRAM up   up \n"

for line in intf_ips.split("\n"):
    match = re.search('(?P<ip>\d+\.\d+\.\d+\.\d+)', line)  
    if match:
        #print(match.groups())
        print(match.groupdict())

matches = re.findall('(?P<ip>\d+\.\d+\.\d+\.\d+)',intf_ips)
print(matches)
import sys
import re
import ipaddress

file = open('./sample_ip_address.txt','r')
ips = []
for line in file:
    # print(line)
    list_ip = re.findall(r'(\d+\.\d+\.\d+\.\d+)',line)
    for item in list_ip:
        try:
            ip = ipaddress.ip_address(item.replace(':',''))
            #ips.append(item.replace(':',''))
            ips.append(ip)
        except:
            pass
        
file.close()
for ip in ips:
    print ('%s ip version is %s' %(ip, ip.version), end="\n" )



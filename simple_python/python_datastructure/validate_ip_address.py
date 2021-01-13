import sys
import ipaddress

try:
    ip = ipaddress.ip_address(sys.argv[1])
    print('%s is correct ip%s address' %(ip,ip.version))
except ValueError:
    print('Invalid IPaddress %s'  % sys.argv[1])
except:
    print('Usage : %s ip' % sys.argv[0])

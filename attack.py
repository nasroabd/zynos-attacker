from netaddr import IPNetwork
import os
for ip in IPNetwork ('41.108.48.1/24'):
    os.system("python code.py "+str(ip))

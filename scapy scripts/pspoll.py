#!/usr/bin/python
import sys
from scapy.all import *
ps = RadioTap()/Dot11(type=1,subtype=10,addr1="00:01:02:03:04:05",addr2="00:01:02:03:04:06")
conf.iface="mon0"
#send(ps)
sendp(ps,inter=.1,loop=1)
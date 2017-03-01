#!/usr/bin/python
import sys
from scapy.all import *
cts = RadioTap()/Dot11(type=1,subtype=12,addr1="00:01:02:03:04:06")
conf.iface="mon0"
#send(cts)
sendp(cts,inter=.01,loop=1)
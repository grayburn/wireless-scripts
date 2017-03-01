#!/usr/bin/python
import sys
from scapy.all import *
rts = RadioTap()/Dot11(type=1,subtype=11,addr1="00:01:02:03:04:06",addr2="00:02:03:04:05:07")
conf.iface="mon0"
#send(rts)
sendp(rts,inter=.01,loop=1)
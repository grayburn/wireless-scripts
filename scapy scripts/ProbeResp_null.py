#!/usr/bin/python
import sys
from scapy.all import *
probeResp = RadioTap()/Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2="00:01:02:03:04:05", addr3="00:01:02:03:04:05")/Dot11ProbeResp(cap='ESS+privacy+short-preamble+short-slot')/Dot11Elt(ID="SSID",info='')/Dot11Elt(ID="Rates",info='\x82\x84\x8b\x96\x0c\x12\x18\x24')/Dot11Elt(ID="DSset",info="\x0b")/Dot11Elt(ID=42, info="\x04")/Dot11Elt(ID=47, info="\x04")/Dot11Elt(ID=50, info="\x0c\x12\x18\x60")
conf.iface = "wlan0mon"
sendp(probeResp,inter=.2,loop=1)
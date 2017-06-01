from scapy.all import *

def PacketHandler(pkt) :
    if pkt.haslayer(Dot11) :
        if pkt.type == 0 and pkt.subtype == 4 :
            if pkt.haslayer(Dot11ProbeReq):
                try:
                    extra = pkt.notdecoded
                    rssi = -(256-ord(extra[-2:-1]))
                except:
                    rssi = -100
                print "WiFi signal strength:", rssi, "dBm of", pkt.addr2, pkt.info
sniff(iface="wlan0mon", prn = PacketHandler)

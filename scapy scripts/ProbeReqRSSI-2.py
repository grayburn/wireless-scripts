from scapy.all import *

client_list = []
threshold = -60 ## signal strength threshold to display
def PacketHandler(pkt) :
    if pkt.haslayer(Dot11) :
        if pkt.type == 0 and pkt.subtype == 4 :
            if pkt.haslayer(Dot11ProbeReq):
                try:
                    extra = pkt.notdecoded
                    rssi = -(256-ord(extra[-2:-1]))
                except:
                    rssi = -100
                if pkt.addr2 not in client_list and rssi > threshold :
 #                   client_list.append(pkt.addr2)
                    print "WiFi signal strength:", rssi, "dBm of", pkt.addr2, pkt.info
sniff(iface="wlan0mon", prn = PacketHandler)

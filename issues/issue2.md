### Issue2
**Setting up the IP addresses on Raspberry Pi. When We add an static ip address to an interface using the file /etc/network/interfaces It is not getting the ip automatically on reboot or it is not persistent** <br/>

*Ans:* Adding the Ip address in the /etc/dhcpd.conf file then it is persistent across reboots.
Insert the following lines in /etc/dhcpd.conf file 
```
iface eth0 inet static
    address 192.168.1.4
    netmask 255.255.255.0
    network 192.168.1.0
    broadcast 192.168.1.255
    gateway 192.168.1.1
```

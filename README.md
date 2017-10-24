# SDN-Project
=====================================

SDN course Project. 

## Installing OVS on Raspberry pi:
=====================================

Make sure Raspberry pi are connected to the internet.
```sh
$ sudo apt-get install openvswitch-switch
```
- Check whether OVS is properly installed in Raspberry Pi. 
- Run the command below  
```sh
$ ovs-vsctl add-br ovs-br1
```
- Check wether a new interface(ovs-br1) is getting created using the command below.
```sh
$ ifconfig
```
### OVS installation done.
=====================================

## Assigning IP to Raspberry pi:
=====================================

1. Using DHCP server: 
If raspberry pi is able to get IP address from some DHCP server and an IP is assigned to raspberry pi, we are half done.
--------------



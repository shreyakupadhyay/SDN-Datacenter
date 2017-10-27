# SDN-Project:

SDN course Project. 

## Installing OVS on Raspberry pi:

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
### OVS installation done:


## Assigning IP to Raspberry pi:

1. Using DHCP server: 
If raspberry pi is able to get IP address from some DHCP server and a IP will be assigned to raspberry pi.
--------------

2. Assigning Static IP address:
```sh
$ sudo vim /etc/network/interfaces
```
- Insert the details below in /etc/network/interfaces file. Change the parameters according to your network.
```
iface eth0 inet static
    address 10.0.0.4
    netmask 255.255.255.0
    network 10.0.0.0
    broadcast 10.0.0.255
    gateway 10.0.0.1
    dns-nameservers 10.0.0.1 8.8.8.8
```
```sh
$ sudo service networking restart
```

## Installing OpenVirteX for Network Slicing:

Use this [link](https://ovx.onlab.us/getting-started/installation/) for installing and starting OpenVirteX.







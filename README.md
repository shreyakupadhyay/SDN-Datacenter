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
$ sudo vim /etc/dhcpcd.conf
```
- Insert the details below in /etc/dhcpcd.conf file. Change the parameters according to your network.
```
interface eth0
static ip_address=192.168.1.4/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1
```

## Installing OpenVirteX for Network Slicing:

Use this [link](https://ovx.onlab.us/getting-started/installation/) for installing and starting OpenVirteX.








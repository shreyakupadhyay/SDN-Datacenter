#!/bin/bash

echo -n "Enter name of ovs bridge to create: "
read bridge

echo -n "Interface name: "
read interface

echo "creating bridge $bridge"
sudo ovs-vsctl add-br $bridge
echo "ovs bridge $bridge created"
echo "adding interface $interface"
sudo ovs-vsctl add-port $bridge $interface
echo "added interface $interface"
sudo ifconfig $interface 0
echo 
echo -n "Enter number of internal interfaces to create other than $bridge: "
read number

echo -n "IP address to add to interface $bridge: "
read ip
echo -n "subnet to add to interface $bridge: "
read subnet
sudo ifconfig $bridge $ip netmask $subnet
sudo ifconfig $bridge up
echo "interface $bridge is up"
for((i=0;i<$number;i++))
	do
		#echo -n "enter name of interface: "
		#read name
		echo "creating internal interface int$i"
		sudo ovs-vsctl add-port $bridge int$i -- set Interface int$i type=internal		
		echo -n "IP address to add to interface int$i: "
		read ip
		echo -n "subnet to add to interface int$i: "
		read subnet
		sudo ifconfig int$i $ip netmask $subnet
		#sudo ip addr add $ip_subnet dev int$
		sudo ifconfig int$i up
		echo "interface int$i is up"
	done
sudo 
#echo "Adding interfaces to bridge $bridge"
#for((i=0;i<$number;i++))
#	do
#		sudo ovs-vsctl add-port $bridge $interface
#		echo "interface int$i added to bridge $bridge"	
#	done


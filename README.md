# Software Defined Datacenter:

# Problem statement:
### Overview: 
Deploying a Software defined network(SDN) on a physical hardware consisting raspberry pi. Performing network slicing and further installing firewall as a service on the sliced network.


### Description:
*The deployed single physical network which contains two types of traffic : Type-1 (Faculty) and Type-2 (students). The Type-1 traffic gets higher bandwidth and lower delays and goes through relaxed firewall rules while Type-2 gets smaller bandwidth per user and best effort delays and restricted rules through firewall.* 

### Tasks:
1. Deploy SDN network on hardware using 6 host(3 raspberry pi and 3 ubuntu complaint system), neatgear L2 switch and SDN software components. This is [task 1](https://github.com/shreyakupadhyay/SDN-Project/blob/master/tasks/task1/NetworkSetup.md). 
2. Performing network slicing using OpenVirtex and mininet. This is [task 2](https://github.com/shreyakupadhyay/SDN-Project/blob/master/tasks/task2/NetworkSlicing.md).
3. Deploying SDN virtual network according to the description provided above.
4. Installing various network functions such as Firewall as a Service(FWaaS) on the above sliced network inside mininet.
 
### Project Documentation:

1. [Network topology](https://github.com/shreyakupadhyay/SDN-Project/blob/master/tasks/task1/Topology.md) deployed using SDN on physical hardware.
2. Procedure followed for various tasks:</br >
  a. For [task 1](https://github.com/shreyakupadhyay/SDN-Project/blob/master/tasks/task1/NetworkSetup.md). </br >
  b. For [task 2](https://github.com/shreyakupadhyay/SDN-Project/blob/master/tasks/task2/NetworkSlicing.md). </br >


### Few references to working VM images for SDN softwares:
1. [Mininet VM](https://github.com/mininet/mininet/releases/download/2.2.2/mininet-2.2.2-170321-ubuntu-14.04.4-server-amd64.zip), a network simulation tool for SDN network.
2. [FloodLight VM](http://opennetlinux.org/binaries/floodlight-vm.zip), a SDN controller.
3. [OpenVirtex VM](http://ovx.onlab.us/wp-content/uploads/ovx-vm-x86_64-2014-10-14.zip), a network slicing tool.









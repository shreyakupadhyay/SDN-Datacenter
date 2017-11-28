## Topology of our SDN network.

### Hardware used:
Three raspberry pi 3, one neatgear L2 switch, three laptops with ubuntu as operating system. 

### Hardware Setup:
All the hosts *host1-host6* are connected with L2 layer neatgear switch with a wired connection.  host1, host2, host3 are the raspberry pi and lies in network 1 while host4, host5, host6 are the ubuntu systems which lies in network 2. OpenVirtual Switch(OVS) is deployed in host3 with (br0) and (int0) interfaces created on host3 using the procedure followed in [NetworkSetup.md](https://github.com/shreyakupadhyay/SDN-Project/blob/master/NetworkSetup.md). You can also use [network setup](https://github.com/shreyakupadhyay/SDN-Project/blob/master/scripts/step1_network_setup.sh) script for directly deploying this network. Further, network IP configurations are described below.


### Network Setup:
host1 - 192.168.1.3/24, gateway - 192.168.1.1 <br />
host2 - 192.168.1.2/24, gateway - 192.168.1.1 <br />
host3 - 192.168.1.1/24(br0) and 192.168.2.1/24(int0)
host4 - 192.168.2.2/24, gateway - 192.168.2.1 <br />
host5 - 192.168.2.3/24, gateway - 192.168.2.1 <br />
host6 - 192.168.2.4/24, gateway - 192.168.2.1 <br />

### Topology Image:
![screenshot from 2017-11-20 16-03-56](https://user-images.githubusercontent.com/9116745/33014513-96ce5904-ce0d-11e7-8842-3860331561fc.png)

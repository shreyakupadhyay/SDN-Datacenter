## Topology of our SDN network.

### Hardware used:
Three raspberry pi 3, one neatgear L2 switch, three laptops with ubuntu as operating system. 

### Hardware Setup:
host1, host2, host3 are raspberry pi's and they are connected with neatgear switch with a wired connection. OpenVirtual 
Switch(OVS) is deployed in host3. (br0) and (int0) interfaces are created on host3 using the procedure followed in [README.md](https://github.com/shreyakupadhyay/SDN-Project)
of the project. host4, host5, host6 are laptops and they are connected with neatgear switch with a wired connection.


### Network Setup:
host1 - 192.168.1.2/24, gateway - 192.168.1.1 <br />
host2 - 192.168.2.2/24, gateway - 192.168.2.1 <br />
host3 - 192.168.1.1/24(br0) and 192.168.2.1/24(int0)

### Topology Image:
![screenshot from 2017-11-20 16-03-56](https://user-images.githubusercontent.com/9116745/33014513-96ce5904-ce0d-11e7-8842-3860331561fc.png)

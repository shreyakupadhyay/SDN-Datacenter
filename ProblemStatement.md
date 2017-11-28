# Problem statement:
### Overview: 
Deploying a Software defined network(SDN) on a physical hardware consisting raspberry pi. Performing network slicing and further installing firewall as a service on the sliced network.


### Description:
*The deployed single physical network which contains two types of traffic : Type-1 (Faculty) and Type-2 (students). The Type-1 traffic gets higher bandwidth and lower delays and goes through relaxed firewall rules while Type-2 gets smaller bandwidth per user and best effort delays and restricted rules through firewall.* 

### Tasks:
1. Deploy SDN network on hardware using 6 host(3 raspberry pi and 3 ubuntu complaint system), neatgear L2 switch and SDN software components. 
2. Performing network slicing using OpenVirtex and mininet.
3. Various rules for on the sliced network as per the problem statement.
4. Installing various network functions such as Firewall as a Service(FWaaS) on the above sliced network inside mininet.
 

Problem Statement:

Here we have four hosts connected to s1 and four hosts connected to s2

Hosts connected to s1 are h1s1v1,h2s1v1,h3s1v2,h4s1v2 and Hosts connected to s2 are h1s2v1,h2s2v1,h3s2v2,h4s2v2

Here v1 corresponds to vlan with vlan id 100, v2 corresponds to vlan with vlan id 200

The code used to generate above topology is vlanhost.py which is obtained by updating vlanhost.py code available in mininet/examples

By running script hosts with in same vlan are able to ping each other and hosts within different vlan are not able to ping each other

Our next task is make host h1s1v1 donot ping h1s2v1 which are connected to different switches s1, s2 respectively and are in same vlan v1 with id 100. 
This is obtained by adding following flow rule

sh ovs-ofctl add-flow s1 icmp,dl_vlan=100,nw_src=10.0.0.1,nw_dst=10.0.0.2,actions=drop

in mininet prompt

If the above thing doesnot work delete flows in s1 and run above command again then it will work

Our next task is make host h2s1v1 ping h3s2v2 ping each other which are in diffrent vlan and connected to different switches s1, s2 respectively. This is
acheived by adding following rules

sh ovs-ofctl add-flow s1 arp,in_port=2,nw_dst=10.0.0.6,actions=mod_vlan_vid=200,output:5 

sh ovs-ofctl add-flow s1 arp,in_port=5,nw_dst=10.0.0.3,actions=mod_vlan_vid=100,output:2

sh ovs-ofctl add-flow s1 icmp,in_port=5,nw_dst=10.0.0.3,actions=mod_vlan_vid=100,output:2

sh ovs-ofctl add-flow s1 icmp,in_port=2,nw_dst=10.0.0.6,actions=mod_vlan_vid=200,output:5

in mininet prompt

Here 10.0.0.3 is ip address of host h2s1v1, 10.0.0.6 is ip address of host h3s2v2 and host h2s1v1 is connected to open flow port 2 of switch s1 and openflow port 5 is connected to switch s2

Output will be as follow:

mininet> pingall
*** Ping: testing ping reachability
h1s1v1 -> X h2s1v1 h2s2v1 X X X X 
h1s2v1 -> X h2s1v1 h2s2v1 X X X X 
h2s1v1 -> h1s1v1 h1s2v1 h2s2v1 X h3s2v2 X X 
h2s2v1 -> h1s1v1 h1s2v1 h2s1v1 X X X X 
h3s1v2 -> X X X X h3s2v2 h4s1v2 h4s2v2 
h3s2v2 -> X X h2s1v1 X h3s1v2 h4s1v2 h4s2v2 
h4s1v2 -> X X X X h3s1v2 h3s2v2 h4s2v2 
h4s2v2 -> X X X X h3s1v2 h3s2v2 h4s1v2 
*** Results: 57% dropped (24/56 received)
mininet>
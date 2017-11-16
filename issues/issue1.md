### Issue1
**Host1 with IP address 192.168.1.2/24 is able to ping both interfaces with IP address 192.168.1.1/24(br0) and 192.168.2.1/24(int0). How host1 is able to ping a interface in another network?** <br />
*Ans:* The traffice here is going through loopback iterface. When we assign IP to a interface a entry gets added to the 
'local' table. And all the routes in this table route over the loopback interface. So, here operating system is deciding that no
packets need to be sent and the kernel itself is replying to these incomming ping packets. <br />

**Have a look to this [link](https://unix.stackexchange.com/questions/122468/how-does-one-capture-traffic-on-virtual-interfaces) for more information.**



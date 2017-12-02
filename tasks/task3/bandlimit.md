#Bandwidth limitng:

##Task 3:
Two students and two faculty are in the college network.
And there is a external internet where two Servers are running
The objective is to rate limit the bandwidth allocated to students and faculty does not have any such limits

####Run script:
Use[https://github.com/shreyakupadhyay/SDN-Project/blob/master/scripts/task3_topo.py]
```
$ sudo python task3_topo.py
```
This setsup the mininet environment and the topology of the simple campus network


####Run script
Use[https://github.com/shreyakupadhyay/SDN-Project/blob/master/scripts/task3_bandwidthlimit.py]
```sh
$ sudo python task3_bandwidthlimit.py 
```

This is for bandwidth limiting for the hosts within the internet.

# Firewall

## Task 3b:
This is a simple firewall as a service that is enabled on the student faculty (Campus) Network.
The current firewall can do all the following services

```
0. Normal action to all switches
1. Students can't ping each-other
2. Block a student ip from accessing Network
3. Block all tcp port 80 from ext1 to students
4. Student1 can talk only to faculty1
5. Block All external traffic to students
```

#### Run script:
To run the firewall first we need to setup the campus network on the mininet.

Use [topo.py](https://github.com/shreyakupadhyay/SDN-Project/blob/master/scripts/task3_topo.py)
```sh
$ sudo mn --custom mesh.py --topo task3_topo.py --controller=remote,ip=127.0.0.1
```
Here we are using a remote Open Day light controller instead of a normal POX controller which is default by the mininet.

To run the firewall as a service some requirements needs to be satisfied. 
```
$ sudo pip install requests
```

To run the script use [step3_firewall_as_service.py](https://github.com/shreyakupadhyay/SDN-Datacenter/blob/master/scripts/step3_firewall_as_service.py)
```
$ python step3_firewall_as_service.py
```

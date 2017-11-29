# Network slicing:

## Task 2:

Use this [link](http://ovx.onlab.us/wp-content/uploads/ovx-vm-x86_64-2014-10-14.zip) to setup the VM for this task.
### Network Setup for slicing:
Building a network topology which consists of 10 switches with 4 hosts associated to each switch. Slicing this network
into two virtual networks controlled by different controllers. Network 1 represents student network while Network 2 represents
faculty network.

#### Network 1(student network):
Each host in this network have maximum bandwidth of **10 MBps**, with a maximum queue size of 1000 packets using the Hierarchical 
Token Bucket rate limiter, loss is in percentage which is set to **2**, delay is with unit with **5ms**. 

#### Network 2(faculty network):
Each host in this network has no fixed bandwidth, no delay, no loss.

#### Run script
Use [networkslice.py](https://github.com/shreyakupadhyay/SDN-Project/blob/master/scripts/step2_network_slicing.py)
```sh
$ sudo python networkslice.py
```

### Slicing the deployed network:
Use [network1.sh](https://github.com/shreyakupadhyay/SDN-Project/blob/master/scripts/step2_network_slicing.sh)
```sh
$ sh network1.sh
```
To check the virtual network deployed in controller, go to http://localhost:10001/ui/index.html.

#### Task 2 done.

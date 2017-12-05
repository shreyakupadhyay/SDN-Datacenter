# Network slicing:

## Task 2:

Use this [link](http://ovx.onlab.us/wp-content/uploads/ovx-vm-x86_64-2014-10-14.zip) to setup the VM for this task.
### Network Setup for slicing:
Building a network topology which consists of 3 switches with 4 hosts associated to each switch. Slicing this network
into two virtual networks controlled by different controllers. Network 1 represents student network while Network 2 represents
faculty network.

#### Network 1(student network):
Each host in this network have maximum bandwidth of **10 MBps**, with a maximum queue size of 1000 packets using the Hierarchical 
Token Bucket rate limiter, loss is in percentage which is set to **2**, delay is with unit with **5ms**. 

#### Network 2(faculty network):
Each host in this network has no fixed bandwidth, no delay, no loss.

#### Run script
Use [networkslice.py](https://github.com/shreyakupadhyay/SDN-Project/blob/master/scripts/step2_network_slicing.py) to slice the network into student and faculty network.
```sh
$ sudo python networkslice.py
```

### Slicing the deployed network:
Use [network1.sh](https://github.com/shreyakupadhyay/SDN-Datacenter/blob/master/scripts/step2_slicing_student_network.sh) for creating virtual student network. 
```sh
$ sh network1.sh
```
![student](https://user-images.githubusercontent.com/9116745/33593327-e77d1978-d9b4-11e7-8d70-53b32bead8b7.png)


Use [network2.sh](https://github.com/shreyakupadhyay/SDN-Datacenter/blob/master/scripts/step2_slicing_faculty_network.sh) for creating virtual faculty network.
```sh
$sh network2.sh
```
![faculty](https://user-images.githubusercontent.com/9116745/33593400-3a536ada-d9b5-11e7-913d-5b88dbc3f249.png)


To check the virtual network deployed in controller, go to http://localhost:10001/ui/index.html for looking into student network and go to http://localhost:20001/ui/index.html for looking into faculty network.

#### Task 2 done.

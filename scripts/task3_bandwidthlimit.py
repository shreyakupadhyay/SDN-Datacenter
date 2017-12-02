# BandLimiting Students link to 1000kbps
#s3 ovs-vsctl set interface s3-eth3 ingress_policing_rate=1000
#s3 ovs-vsctl set interface s3-eth3 ingress_policing_burst=100
import os
print "2 Students Stu1 and Stu2"
print "2 Faculty fac1 and fac2"
print "2 Internet servers running ext1 and ext2"
print "\n\n"
def choices():
    print "1. Rate limit students bandwidth"
    print "2. Rate limit Faculty Bandwidth"
    print "3. Rate Campus external Bandwidth"
    print "Enter your choice"
    cc()

def cc():
    choice = input()
    if(choice == 1):
        while True:
            try:
                speed = int(input("Enter the max wanted link speed in kbps"))
                if speed <0 :
                    raise(Exception, "invalid")
                break
            except:
                print("That is not a valid input")
        burst = speed/10

        cm1 = "sudo ovs-vsctl set interface s3-eth3 ingress_policing_rate="+str(speed)
        cm2 = "sudo ovs-vsctl set interface s3-eth3 ingress_policing_burst="+str(burst)
        os.system(cm1)
        os.system(cm2)
    elif(choice == 2):
        while True:
            try:
                speed = int(input("Enter the max wanted link speed in kbps"))
                if speed <0 :
                    raise(Exception, "invalid")
                break
            except:
                print("That is not a valid input")
        burst = speed/10

        cm1 = "sudo ovs-vsctl set interface s3-eth2 ingress_policing_rate="+str(speed)
        cm2 = "sudo ovs-vsctl set interface s3-eth2 ingress_policing_burst="+str(burst)
        os.system(cm1)
        os.system(cm2)
        
    elif(choice == 3):
        while True:
            try:
                speed = int(input("Enter the max wanted link speed in kbps"))
                if speed <0 :
                    raise(Exception, "invalid")
                break
            except:
                print("That is not a valid input")
        burst = speed/10

        cm1 = "sudo ovs-vsctl set interface s3-eth1 ingress_policing_rate="+str(speed)
        cm2 = "sudo ovs-vsctl set interface s3-eth1 ingress_policing_burst="+str(burst)
        os.system(cm1)
        os.system(cm2)
    else:
        choices()
if __name__ == '__main__':
    choices()
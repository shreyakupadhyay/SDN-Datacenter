import requests
import json
from requests.auth import HTTPBasicAuth
import socket


USERNAME = "admin"
PASSWORD = "admin"
DEFAULT_PORT = "8181"
LOCALHOST = "localhost"
base_url = "http://localhost:8181/restconf/config/opendaylight-inventory:nodes/node/"

student_switch = "openflow:1"
faculty_switch = "openflow:2"
connector_switch = "openflow:3"

drop_action = "<order>0</order><drop-action/>"
ethernet_empty_match = '''
    <ethernet-match>
            <ethernet-type>
                <type>2048</type>
            </ethernet-type>
    </ethernet-match>
    '''

def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False
    return True


def create_flow(flow_id, table=0, priority=6666, match_condition="", action=""):
    flow_id = str(flow_id)
    priority = str(priority)

    flow_actions = "<apply-actions><action>" + action + \
        "</action></apply-actions></instruction></instructions>"
    flow_match_condition = "<match>" + match_condition + "</match>"
    flow_mid = '''<cookie_mask>255</cookie_mask><installHw>false</installHw>'''

    flow_header = '''<flow xmlns="urn:opendaylight:flow:inventory"><strict>false</strict><table_id>''' + table
    flow_header += '''</table_id><id>''' + flow_id + \
        '''</id><instructions><instruction><order>0</order>'''

    flow_footer = '''<cookie>1</cookie>'''
    flow_footer += '''<flow-name>FooXf1</flow-name><priority>''' + \
        str(priority) + "</priority><barrier>false</barrier></flow>"

    flow = flow_header + flow_actions + flow_match_condition + flow_mid + flow_footer
    return flow


def push_flow(flow_id, match_condition="", action="", node="openflow:1", priority="666"):
    table = "0"
    priority = str(priority)
    flow = create_flow(flow_id, table, priority, match_condition, action)
    url = base_url + node + "/table/" + table + "/flow/" + str(flow_id)
    # print flow
    headers = {'content-type': 'application/xml'}
    r = requests.put(url, headers=headers, data=flow,
                     auth=HTTPBasicAuth(USERNAME, PASSWORD))
    # print flow
    # print url
    # print r


def delete_all_flows():
    for i in range(1, 4):
        url = "http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:" + \
            str(i)
        r = requests.delete(url, auth=HTTPBasicAuth(USERNAME, PASSWORD))


def normal_action():
    delete_all_flows()
    priority = 2
    action = '''
                <order>0</order>  
                <output-action>
                    <output-node-connector>NORMAL</output-node-connector>
                    <max-length>60</max-length>
                </output-action>'''
    match = ""
    for i in range(1, 4):
        node = "openflow:" + str(i)
        push_flow(1, match_condition=match, action=action,
                  node=node, priority=priority)


def students_cant_ping():
    normal_action()
    priority = 10
    action = drop_action
    match_condition = ethernet_empty_match + '''
    <ipv4-source>10.0.0.2/32</ipv4-source>
        <ipv4-destination>10.0.0.3/32</ipv4-destination>'''
    node = student_switch
    push_flow(2, match_condition=match_condition,
              action=action, node=node, priority=priority)


def block_student_from_accessing_internet():
    normal_action()
    priority = 15
    while True:
        student_ip = raw_input("Enter a students IP address")
        if (not is_valid_ipv4_address(student_ip)):
            print "Please enter a valid IP address"
        else:
            match_condition= ethernet_empty_match+"<ipv4-source>"+student_ip.strip()+"/32</ipv4-source>"
            push_flow(3,match_condition=match_condition,action=drop_action,node = student_switch,priority=priority)
            break

def block_tcp_80_from_ext1():
    normal_action()
    priority = 20
    match_condition=ethernet_empty_match+"<ipv4-destination>12.12.12.12/32</ipv4-destination>"
    match_condition+="<ip-match><ip-protocol>6</ip-protocol></ip-match>"
    match_condition+="<tcp-destination-port>80</tcp-destination-port>"
    push_flow(4,match_condition=match_condition,action=drop_action,node=student_switch,priority=priority)


def stu1_to_faculty1():
    normal_action()
    priority=22
    match_condition = ethernet_empty_match+"<ipv4-source>10.0.0.2/32</ipv4-source>"
    match_condition+= "<ipv4-destination>10.0.0.101/32</ipv4-destination>"
    action = '''
                <order>0</order>  
                <output-action>
                    <output-node-connector>NORMAL</output-node-connector>
                    <max-length>60</max-length>
                </output-action>'''
    push_flow(5,match_condition=match_condition,action=action,node=student_switch, priority=6666)
    match_condition=ethernet_empty_match+"<ipv4-source>10.0.0.2/32</ipv4-source>"
    action = drop_action
    push_flow(6,match_condition=match_condition,action = action,node=student_switch,priority=priority)

def block_all_external_traffic_to_students():
    normal_action()
    priority=33
    match_condition=ethernet_empty_match+"<ipv4-source>10.0.0.2/24</ipv4-source>"
    match_condition+="<ipv4-destination>10.0.0.2/24</ipv4-destination>"
    action = '''
                <order>0</order>  
                <output-action>
                    <output-node-connector>NORMAL</output-node-connector>
                    <max-length>60</max-length>
                </output-action>'''
    push_flow(7,match_condition,action,student_switch,priority=6666)
    match_condition=ethernet_empty_match+"<ipv4-destination>10.0.0.2/26</ipv4-destination>"
    action = drop_action
    push_flow(8,match_condition,action,student_switch,priority)


def firewall():
    print "0. Normal action to all switches"
    print "1. Students can't ping each-other"
    print "2. Block a student ip from accessing Network"
    print "3. Block all tcp port 80 from ext1 to students"
    print "4. Student1 can talk only to faculty1"
    print "5. Block All external traffic to students"

    choice = input("Enter your choice \t")
    if (choice == 0):
        normal_action()
    elif(choice == 1):
        students_cant_ping()
    elif(choice == 2):
        block_student_from_accessing_internet()
    elif(choice == 3):
        block_tcp_80_from_ext1()
    elif(choice == 4):
        stu1_to_faculty1()
    elif(choice == 5):
        block_all_external_traffic_to_students()
    else:
        firewall()


if __name__ == '__main__':
    firewall()

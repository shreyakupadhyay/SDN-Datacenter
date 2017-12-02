#!/usr/bin/python

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import lg, setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.node import CPULimitedHost

CORES = {
  'SEA': {'dpid': '000000000000010%s'},
  'SFO': {'dpid': '000000000000020%s'},
  'LAX': {'dpid': '000000000000030%s'},
  }

FANOUT = 4
    
class I2Topo(Topo):

  def __init__(self, enable_all = True):
    "Create Internet2 topology."

    # Add default members to class.
    super(I2Topo, self).__init__()

    # Add core switches
    self.cores = {}
    for switch in CORES:
      self.cores[switch] = self.addSwitch(switch, dpid=(CORES[switch]['dpid'] % '0'))

    # Add hosts and connect them to their core switch
    for switch in CORES:
      	for count in xrange(1, FANOUT + 1):
            # Add hosts
            host = 'h_%s_%s' % (switch, count)
            ip = '10.0.0.%s' % count
            mac = CORES[switch]['dpid'][4:] % count
            h = self.addHost(host, ip=ip, mac=mac)
    
    self.addLink('h_SEA_1', 'SEA', bw=10, delay='5ms', loss=2, max_queue_size=1000, use_htb=True)
    self.addLink('h_SEA_2', 'SEA')
    self.addLink('h_SEA_3', 'SEA')
    self.addLink('h_SEA_4', 'SEA')
    self.addLink('h_LAX_1', 'LAX')
    self.addLink('h_LAX_2', 'LAX', bw=10, delay='5ms', loss=2, max_queue_size=1000, use_htb=True)
    self.addLink('h_LAX_3', 'LAX')
    self.addLink('h_LAX_4', 'LAX')
    self.addLink('h_SFO_1', 'SFO')
    self.addLink('h_SFO_2', 'SFO')
    self.addLink('h_SFO_3', 'SFO')
    self.addLink('h_SFO_4', 'SFO')
    # Connect core switches
    self.addLink(self.cores['SFO'], self.cores['SEA'])
    self.addLink(self.cores['SFO'], self.cores['LAX'])


if __name__ == '__main__':
   topo = I2Topo()
   ip = '127.0.0.1'
   port = 6633
   c = RemoteController('c', ip=ip, port=port)
   net = Mininet(topo=topo, autoSetMacs=True, xterms=False, controller=None, link=TCLink)
   net.addController(c)
   net.start()
   print "Hosts configured with IPs, switches pointing to OpenVirteX at %s:%s" % (ip, port)
   CLI(net)
   net.stop()

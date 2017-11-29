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
  'ATL': {'dpid': '000000000000040%s'},
  'IAD': {'dpid': '000000000000050%s'},
  'EWR': {'dpid': '000000000000060%s'},
  'SLC': {'dpid': '000000000000070%s'},
  'MCI': {'dpid': '000000000000080%s'},
  'ORD': {'dpid': '000000000000090%s'},
  'CLE': {'dpid': '0000000000000a0%s'},
  'IAH': {'dpid': '0000000000000b0%s'},
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
        # Connect hosts to core switches
        self.addLink(h, self.cores[switch], bw=10, delay='5ms', loss=2,
                          max_queue_size=1000, use_htb=True)

    # Connect core switches
    self.addLink(self.cores['SFO'], self.cores['SEA'],bw=10)
    self.addLink(self.cores['SEA'], self.cores['SLC'],bw=10)
    self.addLink(self.cores['SFO'], self.cores['LAX'],bw=10)
    self.addLink(self.cores['LAX'], self.cores['SLC'],bw=10)
    self.addLink(self.cores['LAX'], self.cores['IAH'],bw=10)
    self.addLink(self.cores['SLC'], self.cores['MCI'],bw=10)
    self.addLink(self.cores['MCI'], self.cores['IAH'],bw=10)
    self.addLink(self.cores['MCI'], self.cores['ORD'],bw=10)
    self.addLink(self.cores['IAH'], self.cores['ATL'],bw=10)
    self.addLink(self.cores['ORD'], self.cores['ATL'],bw=10)
    self.addLink(self.cores['ORD'], self.cores['CLE'],bw=10)
    self.addLink(self.cores['ATL'], self.cores['IAD'],bw=10)
    self.addLink(self.cores['CLE'], self.cores['IAD'],bw=10)
    self.addLink(self.cores['CLE'], self.cores['EWR'],bw=10)
    self.addLink(self.cores['EWR'], self.cores['IAD'],bw=10)


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

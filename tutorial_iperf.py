from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController, OVSSwitch

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=2):
        switch = self.addSwitch('s1')
        # Python's range(N) generates 0..N-1
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch)

class DoubleSwitchTopo(Topo):
    def build(self):
        switch = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
       
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        self.addLink(h1, switch)
        self.addLink(h2, switch)

        self.addLink(switch, switch2)
        
        self.addLink(h3, switch2)
        self.addLink(h4, switch2)

def simpleTest():
    "Create and test a simple network"
    topo = DoubleSwitchTopo()
    #net = Mininet( topo =topo, controller=RemoteController, switch=OVSSwitch, autoSetMacs=True )
    net = Mininet(
        topo=topo,
        controller=lambda name: RemoteController( name, ip='127.0.0.1' ),
        switch=OVSSwitch,
        autoSetMacs=True )
    net.start()
    # net.build()
    # topo['h1'].start()
    # topo['h2'].start()
    # topo['h3'].start()
    # topo['c0'].start()
    # topo['s1'].start([topo['c0']])
    # topo['s1'].cmd('ovs-vsctl set Bridge s1 protocols=OpenFlow13')
    # topo['c0'].cmd('ryu-manager ryu.app.rest_firewall')
    
    #print "Dumping host connections"
    #dumpNodeConnections(net.hosts)
    #print "Testing network connectivity"
    #net.pingAll()
    CLI ( net )
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
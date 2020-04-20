from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.link import TCLink
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

        self.addLink(h1, switch, cls=TCLink, bw = 1000)
        self.addLink(h2, switch, cls=TCLink, bw = 1000)

        self.addLink(switch, switch2)
        
        self.addLink(h3, switch2)
        self.addLink(h4, switch2)

def simpleTest():

    topo = DoubleSwitchTopo()

    net = Mininet(
        topo=topo,
        controller=lambda name: RemoteController( name, ip='127.0.0.1' ),
        switch=OVSSwitch,
        autoSetMacs=True )
   
    net.start()
    net['h4'].cmd('iperf -s -Z reno -i 1 > resultReno &')
    net['h3'].cmd('iperf -s -Z cubic -i 1 > resultCubic &')

    net['h1'].cmd('iperf -c 10.0.0.4 -Z reno -t 300 &')
    net['h2'].cmd('iperf -c 10.0.0.3 -Z cubic -t 300 &')
    
    CLI ( net )
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
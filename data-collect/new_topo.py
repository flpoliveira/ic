from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.node import RemoteController, OVSSwitch


class NewSwitchTopo(Topo):
    def build(self):
        switch = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')
        switch4 = self.addSwitch('s4')
       
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')

        self.addLink(h1, switch, cls=TCLink, bw=1000)
        self.addLink(h2, switch, cls=TCLink, bw=1000)
        self.addLink(h3, switch, cls=TCLink, bw=1000)
        self.addLink(h4, switch, cls=TCLink, bw=1000)

        self.addLink(switch, switch2)
        self.addLink(switch2, switch3)
        self.addLink(switch3, switch4)
        
        self.addLink(h5, switch4)
        self.addLink(h6, switch4)
        self.addLink(h7, switch4)
        self.addLink(h8, switch4)

def simpleTest():

    topo = NewSwitchTopo()

    net = Mininet(
        topo=topo,
        controller=lambda name: RemoteController( name, ip='127.0.0.1' ),
        switch=OVSSwitch,
        autoSetMacs=True )
    
    
    
    net.start()

    net['h5'].cmd('iperf -s -Z reno -i 1 > resultReno &')
    net['h1'].cmd('iperf -c 10.0.0.5 -Z reno -t 300 &')

    net['h6'].cmd('iperf -s -Z cubic -i 1 > resultCubic &')
    net['h2'].cmd('iperf -c 10.0.0.6 -Z cubic -t 300 &')

    net['h7'].cmd('iperf -s -Z vegas -i 1 > resultVegas &')
    net['h3'].cmd('iperf -c 10.0.0.7 -Z vegas -t 300 &')

    net['h8'].cmd('iperf -s -Z westwood -i 1 > resultWestwood &')
    net['h4'].cmd('iperf -c 10.0.0.8 -Z  westwood -t 300 &')

    
    # net.iperf(hosts=[net['h1'], net['h5']], l4Type= 'TCP', seconds = 5, fmt = '-z reno &' ,port= 5566)
    # net.iperf(hosts=[net['h2'], net['h6']], l4Type= 'TCP', seconds = 5, fmt = '-z reno &' ,port= 5566)
    # net.iperf(hosts=[net['h3'], net['h7']], l4Type= 'TCP', seconds = 5, fmt = '-z reno &' ,port= 5566)
    # net.iperf(hosts=[net['h4'], net['h8']], l4Type= 'TCP', seconds = 5, fmt = '-z reno &' ,port= 5566)


    CLI ( net )
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
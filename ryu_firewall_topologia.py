from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController, OVSSwitch


def simpleTest():
    
    net = Mininet(controller=RemoteController, switch=OVSSwitch, autoSetMacs=True )
    # net = Mininet(
    #     topo=topo,
    #     controller=lambda name: RemoteController( name, ip='127.0.0.1' ),
    #     switch=OVSSwitch,
    #     autoSetMacs=True )

    s1 = net.addSwitch('s1')
    #s2 = net.addSwitch('s2')
    
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    #h4 = net.addHost('h4')

    c0 = net.addController( 'c0', controller=RemoteController, ip='127.0.0.1')

    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    

    net.build()
    c0.start()

    s1.start([c0])
    #s2.start([c0])


    #s1.cmd("ovs-vsctl set Bridge s1 protocols=OpenFlow13")
    #c0.cmd("ryu-manager ryu.app.rest_firewall")

    CLI ( net )
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
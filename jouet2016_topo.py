from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.node import RemoteController, OVSSwitch


class NewSwitchTopo(Topo):
    def build(self):
        Core = self.addSwitch('Core'm dpid="9000000000000000")
        Agg = []
        Agg.append(self.addSwitch('Agg1', dpid="9000000000000001"))
        #Agg.append(self.addSwitch('Agg2'))
        ToR = []
        for i in range(1, 3):
          ToR.append(self.addSwitch('ToR'+str(i), dpid=("900000000000020"+str(i))))
        host = []
        for i in range(1, 11):
          host.append(self.addHost('h'+str(i)))

        self.addLink(Core, Agg[0], cls=TCLink, bw=1000, delay='1ms')
       

        self.addLink(Agg[0], ToR[0], cls=TCLink, bw=1000, delay='0.2ms')

        for i in host:
          self.addLink(i, ToR[0], cls=TCLink, bw=1000, delay='0.1ms')



       
     
def simpleTest():

    topo = NewSwitchTopo()

    net = Mininet(
        topo=topo,
        controller=lambda name: RemoteController( name, ip='127.0.0.1' ),
        switch=OVSSwitch,
        autoSetMacs=True )
    
    
    
    net.start()

    
 

    CLI ( net )
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
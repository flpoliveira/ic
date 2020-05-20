from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.node import RemoteController, OVSSwitch


class NewSwitchTopo(Topo):
    def build(self):
        Core = self.addSwitch('Core', dpid="90000")
        Agg = []
        Agg.append(self.addSwitch('Agg1', dpid="90001"))
        Agg.append(self.addSwitch('Agg2', dpid="90002"))
        ToR = []
        for i in range(1, 5):
          ToR.append(self.addSwitch('ToR'+str(i), dpid=("9020"+str(i))))
        host = []
        for i in range(1, 41):
          host.append(self.addHost('h'+str(i)))

        self.addLink(Core, Agg[0], cls=TCLink, bw=1000, delay='1ms', max_queue_size=60)
        self.addLink(Core, Agg[1], cls=TCLink, bw=1000, delay='1ms', max_queue_size=60)
      
        self.addLink(Agg[0], ToR[0], cls=TCLink, bw=1000, delay='0.2ms', max_queue_size=60)
        self.addLink(Agg[0], ToR[1], cls=TCLink, bw=1000, delay='0.2ms', max_queue_size=60)

        self.addLink(Agg[1], ToR[2], cls=TCLink, bw=1000, delay='0.2ms', max_queue_size=60)
        self.addLink(Agg[1], ToR[3], cls=TCLink, bw=1000, delay='0.2ms', max_queue_size=60)

        for i in range(0, 4):
          for j in range(0, 10):
            self.addLink(host[i*10+j], ToR[i], cls=TCLink, bw=1000, delay='0.1ms', max_queue_size=60)

       



       
     
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
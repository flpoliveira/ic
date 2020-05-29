from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.node import RemoteController, OVSSwitch
from random import randint


class NewSwitchTopo(Topo):
    def build(self):
        Core = self.addSwitch('Core', dpid="1")
        Agg = []
        Agg.append(self.addSwitch('Agg1', dpid="2"))
        Agg.append(self.addSwitch('Agg2', dpid="3"))
        ToR = []
        for i in range(1, 5):
          ToR.append(self.addSwitch('ToR'+str(i), dpid=(str(3+i))))
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
    port = 5000
    for i in range(2,11):
      net['h1'].cmd('iperf3 -s -f K -p '+str(port + i) +' > logs/iperf3log_h'+str(i)+' &')
    mss = 1460
    for i in range(2, 11):
      value = randint(1,100) * mss
      net['h'+str(i)].cmd('iperf3 -c 10.0.0.1 -p '+str(port + i)+' -n '+ str(value)
        +' > logs/h'+str(i)+'Log &')
    
    
   

    CLI ( net )
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
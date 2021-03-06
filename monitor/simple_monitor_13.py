from datetime import datetime
from operator import attrgetter
from ryu.base import app_manager
from ryu.app import simple_switch_13
from ryu.ofproto import ofproto_v1_3
from ryu.ofproto import ether
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, DEAD_DISPATCHER, CONFIG_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ipv4
from ryu.lib.packet import ipv6
from ryu.lib.packet import tcp
from ryu.lib.packet import udp
from ryu.lib.packet import icmp
from ryu.lib.packet import arp
from ryu.lib import hub
from database import myDB


# CONEXAO COM O BANCO
host = 'localhost'
username = 'root'
password = 'root'
database = 'database'
charset = 'utf8mb4'

my_db = myDB(host, username, password, database, charset)



class SimpleMonitor13(simple_switch_13.SimpleSwitch13):

    def __init__(self, *args, **kwargs):
        super(SimpleMonitor13, self).__init__(*args, **kwargs)
        self.datapaths = {}
        self.monitor_thread = hub.spawn(self._monitor)
        
    @set_ev_cls(ofp_event.EventOFPStateChange,
                [MAIN_DISPATCHER, DEAD_DISPATCHER])
    def _state_change_handler(self, ev):
        datapath = ev.datapath
        if ev.state == MAIN_DISPATCHER:
            if datapath.id not in self.datapaths:
                self.logger.debug('register datapath: %016x', datapath.id)
                self.datapaths[datapath.id] = datapath
        elif ev.state == DEAD_DISPATCHER:
            if datapath.id in self.datapaths:
                self.logger.debug('unregister datapath: %016x', datapath.id)
                del self.datapaths[datapath.id]
       

    def _monitor(self):
        while True:
            for dp in self.datapaths.values():
                self._request_stats(dp)
            hub.sleep(10)
    
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        msg = ev.msg
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        my_db.insertSwitchFeatures(("%016x" % msg.datapath_id), msg.n_buffers, msg.n_tables, msg.auxiliary_id, msg.capabilities)
        self.logger.info('OFPSwitchFeatures received: '
                        'datapath_id=0x%016x n_buffers=%d '
                        'n_tables=%d auxiliary_id=%d '
                        'capabilities=0x%08x',
                        msg.datapath_id, msg.n_buffers, msg.n_tables,
                        msg.auxiliary_id, msg.capabilities)

        # install the table-miss flow entry.
        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                          ofproto.OFPCML_NO_BUFFER)]
        self.add_flow(datapath, 0, match, actions)

    def add_flow(self, datapath, priority, match, actions):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        # construct flow_mod message and send it.
        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]
        mod = parser.OFPFlowMod(datapath=datapath, priority=priority,
                                match=match, instructions=inst)
        datapath.send_msg(mod)

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        # get Datapath ID to identify OpenFlow switches.
        dpid = datapath.id
        self.mac_to_port.setdefault(dpid, {})
        
        # analyse the received packets using the packet library.
        pkt = packet.Packet(msg.data)
        eth_pkt = pkt.get_protocol(ethernet.ethernet)
        tcpvar = pkt.get_protocol(tcp.tcp)
        udpvar = pkt.get_protocol(udp.udp)
        ipv4_pkt = pkt.get_protocol(ipv4.ipv4)
        ipv6_pkt = pkt.get_protocol(ipv6.ipv6)
        arp_pkt = pkt.get_protocol(arp.arp)
        icmpvar = pkt.get_protocol(icmp.icmp)
        
        dst = eth_pkt.dst
        src = eth_pkt.src
        if(ipv4_pkt):
            origem = ipv4_pkt.src
            destino = ipv4_pkt.dst
        if(tcpvar):
            port_src = tcpvar.src_port
            port_dst = tcpvar.dst_port
        elif(udpvar):
            port_src = udpvar.src_port
            port_dst = udpvar.dst_port

        # get the received port number from packet_in message.
        in_port = msg.match['in_port']

       # self.logger.info("packet in %s %s %s %s", dpid, src, dst, in_port)

        # learn a mac address to avoid FLOOD next time.
        self.mac_to_port[dpid][src] = in_port

        # if the destination mac address is already learned,
        # decide which port to output the packet, otherwise FLOOD.
        if dst in self.mac_to_port[dpid]:
            out_port = self.mac_to_port[dpid][dst]
        else:
            out_port = ofproto.OFPP_FLOOD

        # construct action list.
        actions = [parser.OFPActionOutput(out_port)]

        # install a flow to avoid packet_in next time.
        if out_port != ofproto.OFPP_FLOOD:
            if(tcpvar and ipv4_pkt):
                match = parser.OFPMatch(eth_type=ether.ETH_TYPE_IP, in_port=in_port, eth_dst=dst, eth_src=src, ip_proto = ipv4_pkt.proto, ipv4_src=origem, ipv4_dst=destino, tcp_src = port_src, tcp_dst = port_dst)
                priority = 999
            elif(udpvar and ipv4_pkt):
                match = parser.OFPMatch(eth_type=ether.ETH_TYPE_IP, in_port=in_port, eth_dst=dst, eth_src=src, ip_proto = ipv4_pkt.proto, ipv4_src=origem, ipv4_dst=destino, udp_src = port_src, udp_dst = port_dst)
                priority = 999
            else:
                priority = 1
                match = parser.OFPMatch(in_port=in_port, eth_dst=dst, eth_src=src)
            self.add_flow(datapath, priority, match, actions)

        # construct packet_out message and send it.
        out = parser.OFPPacketOut(datapath=datapath,
                                  buffer_id=ofproto.OFP_NO_BUFFER,
                                  in_port=in_port, actions=actions,
                                  data=msg.data)
        datapath.send_msg(out)

    def _request_stats(self, datapath):
        self.logger.debug('send stats request: %016x', datapath.id)
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        
        req = parser.OFPFlowStatsRequest(datapath)
        datapath.send_msg(req)

        req = parser.OFPPortStatsRequest(datapath, 0, ofproto.OFPP_ANY)
        datapath.send_msg(req)

   
    @set_ev_cls(ofp_event.EventOFPFlowStatsReply, MAIN_DISPATCHER)
    def _flow_stats_reply_handler(self, ev):
        body = ev.msg.body
        #i = 0
        for stat in body:
            if stat.priority > 1:
                aux = ("%016x" % ev.msg.datapath.id)+';'+str(stat.match['in_port'])+";"+str(stat.instructions[0].actions[0].port)+";"+stat.match['eth_src']+";"+stat.match['eth_dst']
                eth_type = None
                ip_proto = None
                ipv4_src = None
                ipv4_dst = None
                port_src = None
                port_dst = None
                if 'eth_type' in stat.match:
                    eth_type = stat.match['eth_type']
                if 'ip_proto' in stat.match:
                    ip_proto = stat.match['ip_proto']
                if 'ipv4_src' in stat.match:
                    aux = aux + (';%17s' % (stat.match['ipv4_src']))
                    ipv4_src = stat.match['ipv4_src']
                if 'ipv4_dst' in stat.match:
                    aux = aux + (';%17s' % (stat.match['ipv4_dst']))
                    ipv4_dst = stat.match['ipv4_dst']
                if 'tcp_src' in stat.match:
                    aux = aux + ';' + str(stat.match['tcp_src'])
                    port_src = stat.match['tcp_src']
                if 'tcp_dst' in stat.match:
                    aux = aux + ';' + str(stat.match['tcp_dst'])
                    port_dst = stat.match['tcp_dst']
                if 'udp_src' in stat.match:
                    aux = aux + ';' + str(stat.match['udp_src'])
                    port_src = stat.match['udp_src']
                if 'udp_dst' in stat.match:
                    aux = aux + ';' + str(stat.match['udp_dst'])
                    port_dst = stat.match['udp_dst']
               
                my_db.insertFlowStats(hash(aux), ("%016x"%ev.msg.datapath.id),
                            stat.match['in_port'], stat.instructions[0].actions[0].port,
                            stat.match['eth_src'], stat.match['eth_dst'], 
                            stat.packet_count, stat.byte_count, eth_type,
                            ip_proto, ipv4_src, ipv4_dst, port_src, port_dst, stat.priority)

           

    @set_ev_cls(ofp_event.EventOFPPortStatsReply, MAIN_DISPATCHER)
    def _port_stats_reply_handler(self, ev):
        body = ev.msg.body

      
        for stat in sorted(body, key=attrgetter('port_no')):
            print(stat)
            my_db.insertPortStats(("%016x"%ev.msg.datapath.id), stat.port_no,
                            stat.rx_packets, stat.rx_bytes, stat.rx_errors,
                            stat.tx_packets, stat.tx_bytes, stat.tx_errors)
    

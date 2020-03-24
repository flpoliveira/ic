import pymysql.cursors
from operator import attrgetter
from ryu.app import simple_switch_13
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, DEAD_DISPATCHER, CONFIG_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.lib import hub



lista = set()

# def insertPortStats(datapath, port, rx-pkts, rx-bytes, rx-error, txt-pkts, tx-bytes, tx-error):
#             connection = pymysql.connect(host='localhost',
#                                             user='root',
#                                             password='root',
#                                             db='database',
#                                             charset='utf8mb4',
#                                             cursorclass=pymysql.cursors.DictCursor)
#             try:
#                 with connection.cursor() as cursor:
#                     # Create a new record
#                     sql = ("INSERT INTO `portStats`(`datapath`, `port`, `rx-pkts`, `rx-bytes`, `rx-error`, `tx-pkts`, `tx-bytes`, `tx-error`) VALUES ( %s,%s, %s, %s, %s, %s, %s, %s)")
                    
#                     cursor.execute(sql, (datapath, port,
#                             rx-pkts, rx-bytes, rx-error,
#                             tx-pkts, tx_bytes, tx_errors))

#                 # connection is not autocommit by default. So you must commit to save
#                 # your changes.
#                 connection.commit()
#             finally:
#                 connection.close()

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
        # elif ev.state == CONFIG_DISPATCHER:
        #     if datapath.id in self.datapaths:
        #         self.logger.debug('register datapath: %016x', datapath.id)
        #         self.datapaths[datapath.id] = datapath

    def _monitor(self):
        while True:
            for dp in self.datapaths.values():
                self._request_stats(dp)
              #  self._request_switch_features(dp)
            hub.sleep(10)
    
    # def _request_switch_features(self, datapath):
    #     self.logger.debug('send switch features request: %016x', datapath.id)
    #     ofproto = datapath.ofproto
    #     parser = datapath.ofproto_parser

    #     req = parser.OFPSwitchFeatures(datapath)
    #     datapath.send_msg(req)

    def _request_stats(self, datapath):
        self.logger.debug('send stats request: %016x', datapath.id)
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        
        req = parser.OFPFlowStatsRequest(datapath)
        datapath.send_msg(req)

        req = parser.OFPPortStatsRequest(datapath, 0, ofproto.OFPP_ANY)
        datapath.send_msg(req)

    # @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    # def switch_features_handler(self, ev):
    #     msg = ev.msg
        
    #     try:
    #         with connection.cursor() as cursor:
    #             # Create a new record
    #             sql = ("INSERT INTO `switch`(`auxiliary_id`, `n_tables`, `n_buffers`, `datapath_id`, `capabilities`) VALUES ( %d,%d,%d,'0x%016x','0x%08x')")
    #             cursor.execute(sql, (msg.auxiliary_id, msg.n_tables, msg.n_buffers, msg.datapath_id, msg.capabilities))

    #         # connection is not autocommit by default. So you must commit to save
    #         # your changes.
    #         connection.commit()
    #     finally:
    #         connection.close()

    #     self.logger.info('OFPSwitchFeatures received: '
    #                     'datapath_id=0x%016x n_buffers=%d '
    #                     'n_tables=%d auxiliary_id=%d '
    #                     'capabilities=0x%08x',
    #                     msg.datapath_id, msg.n_buffers, msg.n_tables,
    #                     msg.auxiliary_id, msg.capabilities)

    @set_ev_cls(ofp_event.EventOFPFlowStatsReply, MAIN_DISPATCHER)
    def _flow_stats_reply_handler(self, ev):
        body = ev.msg.body

        self.logger.info('datapath         '
                         'in-port  eth-dst           '
                         'out-port packets  bytes')
        self.logger.info('---------------- '
                         '-------- ----------------- '
                         '-------- -------- --------')
        for stat in sorted([flow for flow in body if flow.priority == 1],
                           key=lambda flow: (flow.match['in_port'],
                                             flow.match['eth_dst'])):
            print(stat)
            aux = ('%016x %8x %17s %8x %8d %8d'%
                             (ev.msg.datapath.id,
                             stat.match['in_port'], stat.match['eth_dst'],
                             stat.instructions[0].actions[0].port,
                             stat.packet_count, stat.byte_count))
            self.logger.info(aux)
            # if aux not in lista:
            #     lista.add(aux)
            #     connection = pymysql.connect(host='localhost',
            #                                 user='root',
            #                                 password='root',
            #                                 db='database',
            #                                 charset='utf8mb4',
            #                                 cursorclass=pymysql.cursors.DictCursor)
            #     try:
            #         with connection.cursor() as cursor:
            #             # Create a new record
            #             sql = ("INSERT INTO `flowStats`(`datapath`, `in-port`, `eth-dst`, `out-port`, `packets`, `bytes`) VALUES ( %s,%s, %s, %s, %s, %s)")
                        
            #             cursor.execute(sql, (ev.msg.datapath.id,
            #                     stat.match['in_port'], stat.match['eth_dst'],
            #                     stat.instructions[0].actions[0].port,
            #                     stat.packet_count, stat.byte_count))

            #         # connection is not autocommit by default. So you must commit to save
            #         # your changes.
            #         connection.commit()
            #     finally:
            #         connection.close()
                

    @set_ev_cls(ofp_event.EventOFPPortStatsReply, MAIN_DISPATCHER)
    def _port_stats_reply_handler(self, ev):
        body = ev.msg.body

        self.logger.info('datapath         port     '
                         'rx-pkts  rx-bytes rx-error '
                         'tx-pkts  tx-bytes tx-error')
        self.logger.info('---------------- -------- '
                         '-------- -------- -------- '
                         '-------- -------- --------')
        for stat in sorted(body, key=attrgetter('port_no')):
            print(stat)
            aux = ('%016x %8x %8d %8d %8d %8d %8d %8d' %
                             (ev.msg.datapath.id, stat.port_no,
                             stat.rx_packets, stat.rx_bytes, stat.rx_errors,
                             stat.tx_packets, stat.tx_bytes, stat.tx_errors))
            self.logger.info(aux)
            # if aux not in lista:
            #     lista.add(aux)
            #     insertPortStats(ev.msg.datapath.id, stat.port_no,
            #                     stat.rx_packets, stat.rx_bytes, stat.rx_errors,
            #                     stat.tx_packets, stat.tx_bytes, stat.tx_errors)
        

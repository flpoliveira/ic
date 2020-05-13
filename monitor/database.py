import pymysql.cursors

class myDB:
    def __init__(self, host, username, password, database, charset):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.charset = charset

    def insertSwitchFeatures(self, dpid, n_buffers, n_tables, auxiliary_id, capabilities):
        connection = pymysql.connect(host=self.host,
                                                user=self.username,
                                                password=self.password,
                                                db=self.database,
                                                charset=self.charset,
                                        cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `dpid` FROM `switch` WHERE `dpid`=%s"
                cursor.execute(sql, (dpid))
                result = cursor.fetchone()

                if not result:
                    with connection.cursor() as cursor:
                        # Create a new record
                        sql = ("INSERT INTO `switch`(`dpid`, `n_buffers`, `n_tables`, `auxiliary_id`, `capabilities`)"
                                " VALUES ( %s,%s, %s, %s, %s)")
                        
                        cursor.execute(sql, (dpid, n_buffers,
                                n_tables, auxiliary_id, capabilities))

                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()
        finally:
            connection.close()
    def insertPortStats(self, datapath, port, rx_pkts, rx_bytes, rx_error, tx_pkts, tx_bytes, tx_error):
        connection = pymysql.connect(host=self.host,
                                        user=self.username,
                                        password=self.password,
                                        db=self.database,
                                        charset=self.charset,
                                        cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `rx-packets`, `rx-bytes`, `rx-error`,`tx-packets`,`tx-bytes`,`tx-error` FROM `portStats` WHERE `dpid`=%s AND `port_no`=%s"
                cursor.execute(sql, (datapath, port))
                result = cursor.fetchone()

                if not result:
                    # Create a new record
                    sql = ("INSERT INTO `portStats`(`dpid`, `port_no`, `rx-packets`, `rx-bytes`, `rx-error`, `tx-packets`, `tx-bytes`, `tx-error`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)")
                    
                    cursor.execute(sql, ( datapath, port,
                            rx_pkts, rx_bytes, rx_error,
                            tx_pkts, tx_bytes, tx_error))
                else:
                    if not(result['rx-packets'] ==  rx_pkts and result['rx-bytes'] ==  rx_bytes and result['rx-error'] == rx_error and result['tx-packets'] == tx_packets
                                    and result['tx-bytes'] == tx_bytes and result['tx-error'] == tx_error):
                        sql = ("UPDATE `portStats` SET `rx-packets`=%s, `rx-bytes`=%s, `rx-error`=%s, `tx-packets`=%s, `tx-bytes`=%s,  `tx-error` = %s WHERE `dpid`=%s AND `port_no`=%s")
                        cursor.execute(sql, (rx_pkts, rx_bytes, rx_error,
                            tx_pkts, tx_bytes, tx_error, datapath,port))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()
    
    def insertFlowStats(self, hsh, dpid, in_port, out_port, eth_src, eth_dst, 
                    packets, bytes, eth_type, ip_proto, ipv4_src, 
                    ipv4_dst, port_src, port_dst, priority):
        connection = pymysql.connect(host=self.host,
                                        user=self.username,
                                        password=self.password,
                                        db=self.database,
                                        charset=self.charset,
                                        cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `packets`,`bytes`  FROM `flowStats` WHERE `hash`=%s"
                cursor.execute(sql, (hsh))
                result = cursor.fetchone()

                if not result:
                    # Create a new record
                    sql = ("INSERT INTO `flowStats`(`hash`, `dpid`, `in-port`, `out-port`, `eth-src`, `eth-dst`, `packets`, `bytes`, `eth-type`, `ip-proto`, `ipv4-src`, `ipv4-dst`, `port-src`, `port-dst`, `priority`) VALUES ( %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    
                    cursor.execute(sql, (hsh, dpid, in_port, out_port, eth_src, eth_dst, packets, bytes, eth_type, ip_proto,
                                            ipv4_src, ipv4_dst, port_src, port_dst, priority))
                else:
                    if not (result['packets'] == packets and result['bytes'] == bytes):
                        sql = ("UPDATE `flowStats` SET `dpid`=%s, `in-port`=%s, `out-port`=%s, `eth-src`=%s, `eth-dst`=%s, `packets`=%s,  `bytes` = %s, `eth-type` = %s, `ip-proto`= %s, `ipv4-src` = %s, `ipv4-dst` = %s, `port-src` = %s, `port-dst`= %s, `priority` = %s WHERE `hash` = %s")
                        cursor.execute(sql, (dpid, in_port, out_port, eth_src, eth_dst, packets, bytes, eth_type, ip_proto,
                                                ipv4_src, ipv4_dst, port_src, port_dst, priority, hsh))
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()
    
    def cleanDatabase(self):
        connection = pymysql.connect(host=self.host,
                                        user=self.username,
                                        password=self.password,
                                        db=self.database,
                                        charset=self.charset,
                                        cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                sql = "SET FOREIGN_KEY_CHECKS=0;"
                cursor.execute(sql);
                sql = "TRUNCATE TABLE `flowStats`;"
                cursor.execute(sql);
                sql = "TRUNCATE TABLE `portStats`;"
                cursor.execute(sql);
                sql = "TRUNCATE TABLE `switch`;"
                cursor.execute(sql);
                sql = "SET FOREIGN_KEY_CHECKS=1;"
                cursor.execute(sql);
                
                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()
        finally:
            connection.close()
        





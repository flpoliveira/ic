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
    def insertPortStats(self, hsh, datapath, port, rx_pkts, rx_bytes, rx_error, tx_pkts, tx_bytes, tx_error):
        connection = pymysql.connect(host=self.host,
                                        user=self.username,
                                        password=self.password,
                                        db=self.database,
                                        charset=self.charset,
                                        cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `hash` FROM `portStats` WHERE `hash`=%s"
                cursor.execute(sql, (hsh))
                result = cursor.fetchone()

                if not result:
                    # Create a new record
                    sql = ("INSERT INTO `portStats`(`hash`, `dpid`, `port_no`, `rx-packets`, `rx-bytes`, `rx-error`, `tx-packets`, `tx-bytes`, `tx-error`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    
                    cursor.execute(sql, (hsh, datapath, port,
                            rx_pkts, rx_bytes, rx_error,
                            tx_pkts, tx_bytes, tx_error))

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
                sql = "SELECT `hash` FROM `flowStats` WHERE `hash`=%s"
                cursor.execute(sql, (hsh))
                result = cursor.fetchone()

                if not result:
                    # Create a new record
                    sql = ("INSERT INTO `flowStats`(`hash`, `dpid`, `in-port`, `out-port`, `eth-src`, `eth-dst`, `packets`, `bytes`, `eth-type`, `ip-proto`, `ipv4-src`, `ipv4-dst`, `port-src`, `port-dst`, `priority`) VALUES ( %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                    
                    cursor.execute(sql, (hsh, dpid, in_port, out_port, eth_src, eth_dst, packets, bytes, eth_type, ip_proto,
                                            ipv4_src, ipv4_dst, port_src, port_dst, priority))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        finally:
            connection.close()




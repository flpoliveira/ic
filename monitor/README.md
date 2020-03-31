</details>

## Guardando as informações do monitor em uma database

<details>

<summary>Port Stats - Clique para expandir </summary>

#### Body do JSON

| Atributo | Descrição | Exemplo |
| --- | --- | --- |
| dpid | Datapath ID | "1" |
| length | Length of this entry | 88 |
| table_id | Table ID | 0 |
| durantion_sec | Time flow has been alive in seconds | 2 |
| durantion_nsec | Time flow has been alive in nanoseconds beyond duration_sec | 6.76e+08 |
| priority | Priority of the entry | 11111 |
| idle_timeout | Number of seconds idle before expiration | 0 |
| hard_timeout | Number of seconds before expiration | 0 |
| flags | Bitmap of OFPFF_* flags | 1 |
| cookie | Opaque controller-issued identifier | 1 |
| packet_count | Number of packets in flow | 0 |
| byte_count | Number of bytes in flow | 0 |
| match | Fields to match | {"in_port":1} |
| actions | Instruction set | ["OUTPUT:2"] |

#### Valores obtidos em ambiente real

| Atributo | Valor |
| --- | --- |
| port_no | 2 |
| rx_packets | 15 |
| tx_packets | 39 |
| rx_bytes | 1206 |
| tx_bytes | 2818 |
| rx-dropped | 0 |
| tx_dropped | 0 |
| rx_errors | 0 |
| tx_errors | 0 |
| rx_frame_err | 0 |
| rx_over_err | 0 |
| rx_crc_err | 0 |
| collisions | 0 |
| duration_sec | 0 |
| duration_nsec | 596000000 |




</details>

<details>
<summary>FlowStats - Clique para expandir</summary>

#### Body do JSON

| Atributo | Descrição | Exemplo |
| --- | --- | --- |
| dpid | Datapath ID | "1" |
| length | Length of this entry | 88 |
| table_id | Table ID | 0 |
| duration_sec | Time flow has been alive in seconds | 2 |
| duration_nsec | Time flow has been alive in nanoseconds beyond duration_sec | 6.76e+08 |
| priority | Priority of the entry | 11111 |
| idle_timeout | Number of seconds idle before expiration | 0 |
| hard_timeout | Number of seconds before expiration | 0 |
| flags | Bitmap of OFPFF_* flags | 1 |
| cookie | Opaque controller-issued identifier | 1 |
| packet_count | Number of packet in flow | 0 |
| byte_count | Number of bytes in flow | 0 |
| match | Fields to match | {"in_port":1} |
| actions | Instruction set | ["OUTPUT:2"] |

#### Valores obtidos em ambiente real

| Atributo | Valor |
| --- | --- |
| byte_count | 630 |
| cookie | 0 |
| duration_nsec | 48000000 |
| duration_n_sec | 1018 |
| flags | 0 |
| hard_timeout | 0 |
| idle_timeout | 0 |
| instructions | [OFPInstructionActions(actions=[OFPActionOutput(len=16, max_len=65509, port=1, type=0), len=24, type=4])] |
| length | 96 |
| match | OFPMatch(oxm_fields={'eth_dst': '00:00:00:00:00:01', 'in_port': 2}) |
| packet_count | 7 |
| priority | 1 |
| table_id | 0 |


</details>

* [Link interessante que achei sobre OXM Fields](http://flowgrammable.org/sdn/openflow/message-layer/match/#tab_ofp_1_3)
* [Link interessante que achei sobre REST/API Ryu para pegar informações](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html#get-all-flows-stats)

### Modelo conceitual do banco

<img src='img/database.png' alt='Modelo conceitual do banco'>

<p>Uma base de dados foi desenvolvida para este sistema e a o código <b>simple_monitor_13.py </b> foi adaptado para que seus monitoramentos forem inseridos neste banco</p>
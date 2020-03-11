# Iniciação Cientifica

#Dicas
- O comando "sudo mn -c" limpa as topologias criadas no mininet
- A biblioteca CLI serve para que ao executar uma topologia em python, ela permaneça sendo executada


## Tutorial executado para Ryu
[https://www.youtube.com/watch?v=BqcjuGxDYN4]


Pré-requisitos
- Mininet instalado
- Ryu instalado

1 - Download do arquivo mininet-topologies
2 - Unzip no lugar desejado
3 - Abrir 2 terminais:
    3.1 - Em um terminal rodar o comando "sudo mn --custom minimal.py --topo minimal --mac --switch ovs --controller remote"
    3.1.1 - Esse comando da inicio a topologia definida no arquivo minimal.py
    3.2 - No outro terminal rodar este comando "ryu-manager ryu.app.simple_switch_13 ryu.app.ofctl_rest"


sudo mn --custom datacenterBasic.py --topo dcbasic --mac --switch ovs --controller remote

===============

# Tutorial de Ryu - Criando meu primeiro código

## Material usado
[Link 1](https://ryu.readthedocs.io/en/latest/writing_ryu_app.html)

Para configurar switches, roteadores, etc. É necessário que escreva uma aplicação Ryu, a aplicação Ryu é formada por scripts em python e ela diz ao Ryu como você quer gerenciar a rede e o Ryu irá configurar os equipamentos usando o protocolo OpenFlow para mim.

Ao criar o arquivo em python utilizando o nome que desejar para rodar basta fazer
"ryu-manager diretorio/script.py"

ryu-manager l2.py ryu.app.ofctl_rest


# Resumo da Documentação Ryu

* **set_ev_cls** -> decorator, indica quando a função decorada deve ser chamada 
    - **Primeiro argumento** indica a que tipo de evento a função é chamada.
        - ofp_event.EventOFPSwitchFeatures
        - ofp_event.EventOFPPacketIn
    - **Segundo argumento** indica o estado do switch
        - MAIN_DISPATCHER
* **OFPActionOutput** -> junto com o packet_out especifica a qual porta do switch o pacote sera mandando
    * **OFPP_FLOOD** -> é flag para indicar todas as portas
* **OFPPacketOut** -> classe para construir o pacote de saida
 * **send_msg** -> método da classe Datapath, ao colocar uma mensagem do tipo OpenFlow, a mensagem sera comutada pelo switch.

 ===============

# Experiência Firewall RYU
[Link 2](https://osrg.github.io/ryu-book/en/html/rest_firewall.html)

* Execute o comando  "sudo mn --topo single,3 --mac --switch ovsk --controller remote -x"
    * para criar a topologia da rede.
* Execute o comando e em seguida "s1 ovs-vsctl set Bridge s1 protocols=OpenFlow13".
    * xterm abre uma janela do XMing para o switch
    * O próximo comando define a versão do OpenFlow utilizada em cada roteador
* Agora de start ao *Ryu* "xterm c0" com o comando "ryu-manager ryu.app.rest_firewall"
* Jogue o seguinte JSON em um terminal qualquer, sem ser o do mininet, para ativar o firewall no switch desejado.
```json
curl -X PUT http://localhost:8080/firewall/module/enable/0000000000000001
  [
    {
      "switch_id": "0000000000000001",
      "command_result": {
        "result": "success",
        "details": "firewall running."
      }
    }
  ]
```
* Para adicionar uma regra que permita a conversa de protocolos do tipo ICMP entre "h1" e "h2"
```json
 curl -X POST -d '{"nw_src": "10.0.0.1/32", "nw_dst": "10.0.0.2/32", "nw_proto": "ICMP"}' http://localhost:8080/firewall/rules/0000000000000001
  [
    {
      "switch_id": "0000000000000001",
      "command_result": [
        {
          "result": "success",
          "details": "Rule added. : rule_id=1"
        }
      ]
    }
  ]

```
```json
curl -X POST -d '{"nw_src": "10.0.0.2/32", "nw_dst": "10.0.0.1/32", "nw_proto": "ICMP"}' http://localhost:8080/firewall/rules/0000000000000001
  [
    {
      "switch_id": "0000000000000001",
      "command_result": [
        {
          "result": "success",
          "details": "Rule added. : rule_id=2"
        }
      ]
    }
  ]
```
    

ler pagina 366 5.7 Kurose
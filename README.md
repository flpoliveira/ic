# Iniciação Cientifica

#Dicas
- O comando "sudo mn -c" limpa as topologias criadas no mininet
- A biblioteca CLI serve para que ao executar uma topologia em python, ela permaneça sendo executada


#Tutorial executado para Ryu
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

# Tutorial de Ryu - Criando meu primeiro código

## Material usado
[Link 1](https://ryu.readthedocs.io/en/latest/writing_ryu_app.html)

[Link 2](https://osrg.github.io/ryu-book/en/html/rest_firewall.html)

Para configurar switches, roteadores, etc. É necessário que escreva uma aplicação Ryu, a aplicação Ryu é formada por scripts em python e ela diz ao Ryu como você quer gerenciar a rede e o Ryu irá configurar os equipamentos usando o protocolo OpenFlow para mim.

Ao criar o arquivo em python utilizando o nome que desejar para rodar basta fazer
"ryu-manager diretorio/script.py"

ryu-manager l2.py ryu.app.ofctl_rest

# Documentação Ryu

* set_ev_cls -> decorator, indica quando a função decorada deve ser chamada 
    - **Primeiro argumento** indica a que tipo de evento a função é chamada.
        - ofp_event.EventOFPSwitchFeatures
        - ofp_event.EventOFPPacketIn
    - **Segundo argumento** indica o estado do switch
        - MAIN_DISPATCHER


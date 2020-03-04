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
[https://ryu.readthedocs.io/en/latest/writing_ryu_app.html]
[https://osrg.github.io/ryu-book/en/html/rest_firewall.html]
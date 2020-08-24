#### Esse repositório contém o material que usei durante minha Iniciação cientifica.

Neste README irei escrever um resumo de tudo que aconteceu durante esse período.

Explique o problema que você estudou, a abordagem que tentou usar e o cenário experimental que foi montado.

--- 

### Escalonamento de Tarefas Comunicantes guiado por Deep Learning

##### O Problema

* Grades computacionais possuem um alto tráfego de pacotes e inúmeros algoritmos são implementados para otimizar esse processo de modo que os gargalos sejam minimizados, mas com cenários tão complexos e diferentes a escolha de um algoritmo apropriado é muito difícil. 

* O Deep Learning é uma subárea do aprendizado de máquina que pode ser usado para tomadas de decisões, seu diferencial comparado as outras técnicas de aprendizado de máquina é que pode ser treinado em hardwares específico que acelera o processo. 

#####  Objetivo

* Desenvolver um escalonador que indicasse, baseado em técnicas de deep learning, qual o melhor comportamento para que a comunicação gere o menor número de gargalos.


#### Objetivo específicos

* Desenvolver uma topologia similar a um Data Center.
* Escolher a melhor tecnologia para um controlador da rede.
* Desenvolver um controlador que monitorasse e coletasse o maior número possível de dados sobre o tráfego do data center.
* Construir um banco de dados para guardar as informações dos tráfegos.
* Utilizar o Deep Learning sobre os dados obtidos.
* Construir um escalonador que baseado nas tomadas de decisões do deep learning escolhesse o melhor método para o tráfego da comunicação.


#### Fundamentação teórica

<details>
<summary>ESCALONAMENTO DE TAREFAS COMUNICANTES GUIADO POR DEEP LEARNING - Autor: Kleiton Pereira</summary>

Neste trabalho Kleiton propõe o uso de um escalonador de tarefas comunicantes utilizando o Deep Learning como uma solução multi-objetiva, escalável, de propósito geral e altamente configurável. Ele diz que a solução possui um agente que pode ser treinado para otimizar métricas que o desenvolvedor por escolher.
</details>

<details>
<summary>GERENCIAMENTO DE RECURSOS ORIENTADO A ENERGIA COM DEEP REINFORCEMENT LEARNING EM GRADES COMPUTACIONAIS - Autor: Lucas Camelo Casagrande</summary>

Nesta dissertação Lucas fala sobre o que são grades computacionais e suas diferentes classificações e objetivos, além disso ele explica sobre a construção de um agente de Deep Reinforcement Learning e seu objetivo é adotar o aprendizado de máquina para tomar as complexas decisões dentro de uma grade computacional para diminuir o consumo de energia.
</details>

<details>
<summary>OpenFlow: Enabling Innovation in Campus Networks </summary>

* Autores:
    * Nick McKeown
    * Tom Anderson
    * Hari Balakrishnan
    * Guru Parulkar
    * Larry Peterson
    * Jennifer Rexford
    * Scott Shenker
    * Jonathan Turner

Neste artigo é discutido a proposta do OpenFlow um protocolo que utilizamos hoje em dia para aplicações de SDNs, o Open Flow nasceu de pesquisadores que não conseguiam aplicar seus experimentos de redes em ambientes reais sem afetar a rede dos demais utilizadores, logo surge a necessidade da criação de uma entidade central que pudesse monitorar e controlar os aparelhos da rede para que o tráfego pudesse ser administrado. 

</details>

<details>
<summary>OTCP: SDN-Managed Congestion Control for Data Center Networks</summary>

* Autores:
    * Simon Jouet
    * Colin Perkins
    * Dimitrios Pezaros

Neste artigo é proposto uma variante do TCP, já que o TCP não possui um bom comportamento para o tráfego de um Data Center onde a latência é super baixa e o número de tráfego é muito grande. Então a variante do TCP chamada OTCP que eles propõe utilizam um SDN que faz o controle des paramêtros como controle de janela, tamanho do buffer, entre outros para que não tenha tanto gargalo na rede.

</details>


#### Tecnologias escolhidas

* Mininet
    * Para a construção da topologia utilizamos o Mininet, um emulador de uma rede com hosts, switchs, controladores tudo de forma virtual e que pode ser instalado em uma máquina virtual linux. 
* RYU 
    * O Ryu foi atrelado ao Mininet para a construção do Controlador, o RYU é um framework que fornece uma API para o gerenciamento da rede como SDN. Ele suporta diferentes versões do OpenFlow 1.0, 1.2, 1.3, entre outras.
* MySQL
    * Para o desenvolvimento do banco de dados para coletar os dados do tráfego do data center.
#### Topologia Desenvolvida

* Utilizando o mininet desenvolvemos a seguinte topologia, composta por 4 hosts e 2 switchs.

<img src="/img/topologia_2_switch.png">

#### Experimento com Firewall

* Como parte de aprendizado de como utilizar o RYU resolvemos fazer o seguinte experimento, onde configuramos os Switchs da topologia de tal forma que a comunicação direta entre o host 1 e o 4 fosse bloqueada, mas já a comunicação entre os demais nós da rede não pode ser afetada.
* Atingimos nosso objetivo e serviu como uma base de aprendizado para conseguirmos trabalhar com o RYU.

#### Banco de Dados

* Para coletar os dados do tráfego dos switchs, nós desenvolvemos um banco de dados utilizando o MySQL e nesse banco podemos guardar informações sobre o tráfego, como origem, destino, porta de entrada, porta de saida, número de pacotes, número de bytes do tráfego, ipv4 de origem e ipv4 de destino, entre outras informações.

#### Controlador para coleta de dados

* Com uma topologia criada no Mininet e com o controlador RYU instalado e com o Banco de Dados desenvolvido em MySQL, foi possível criar um controlador na linguagem Python que pede por formações estatísticas dos switch que pertencem a topologia a cada 10 segundos e as guarda no banco de dados.

* Com essa coleta é possível estabelecer nosso primeiro objetivo, onde no futuro esses dados podem ser utilizados para a construção do Deep Learning.


#### Trabalhos Futuros

* Desenvolver o agente do Deep Learning para que ele aprenda sobre os dados coletados
* Criar o escalonador para que tome as decisões para diferentes cenários baseado nos dados coletados.
* Testar o desempenho do escalonador comparado a outras técnicas de minimização de gargalos em data centers.


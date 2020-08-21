#### Esse repositório contém o material que usei durante minha Iniciação cientifica.

Neste README irei escrever um resumo de tudo que aconteceu durante esse período.

Explique o problema que você estudou, a abordagem que tentou usar e o cenário experimental que foi montado.

--- 

### Escalonamento de Tarefas Comunicantes guiado por Deep Learning

##### O Problema

* Grades computacionais possuem um alto tráfego de pacotes, e inúmeros algoritmos são implementados para otimizar esse processo de modo que os gargalos sejam minimizados, mas com cenários tão complexos e diferentes a escolha de um algoritmo apropriado é muito difícil. 

* O Deep Learning é uma subárea do aprendizado de máquina que pode ser usado para tomadas de decisões, seu diferencial comparado as outras técnicas de aprendizado de máquina é que pode ser treinado em hardwares específico que acelera o processo. 

#####  Objetivo

* Desenvolver um escalonador que indicasse, baseado em técnicas de deep learning, qual o melhor comportamento para que a comunicação gere o menor número de gargalos.


#### Objetivo específicos

* Desenvolver uma topologia similar a um Data Center.
* Escolher a melhor tecnologia para um controlador da rede.
* Desenvolver um controlador que monitorasse e coletasse o maior número possível de dados sobre o tráfego do data center.
* Construir um banco de dados para guardar as informações dos tráfegos.
* Utilizar o Deep Learning sobre os dados obtidos.
* Construir um escalonador que baseado nas tomadas de decisões do deep learning escolhesse o melhor método para o tráfego de comunicação.


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
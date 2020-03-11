## Resumo Leitura "Redes de computadores e a Internet: uma abordagem top-down" Kurose 6ª Edição.
<details>
  <summary>Item 5.7 Um dia na vida de uma solicitação de página Web pg366</summary>

### Cenário
<p>Bob é um estudante e conecta seu notebook ao comutador Ethernet da sua escola e faz o download de uma página Web (www.google.com)</p>
<img src="/img/bob_cenario.png" alt="Cenario Bob"/>

------

### DHCP , UDP, IP e Ethernet

* DNS está fora da rede interna, o roteador da escola é conectado a um ISP (Fornecedor de acesso a internet), servidor DHCP no roteador

1. DHCP - Computador conecta a uma rede sem um IP, IP Dinamico
    * Notebook envia um pacote para o destino (255.255.255.255) com endereço de origem IP (0.0.0.0)
    * O quadro desse pacote tem destino MAC (FF:FF:FF:FF:FF:FF) com o mac do Notebook do Bob (00:16:D3:23:68:8A)
    * O roteador recebe a requisição DHCP do notebook.
    * Cria uma mensagem ACK DHCP contendo um endereço de IP da sua faixa de rede. Assim como ip do servidor DNS, endereço IP para o roteador de borda (gateway) e o bloco da sub-rede (/24) (Máscara da rede) 
    * Toda essa mensagem tem o endereço Mac de Origem do roteador (00:22:6B:45:1F:1B) e endereço de destino do notebook do Bob (00:16:D3:23:68:8A)
    * Esse pacote(quadro) passa pelo comutador e vai direto ao destino, pois o comutador já conhece esse caminho com a autoaprendizagem.
    * O notebook do Bob recebe esse ACK DHCP e atribui as suas configurações de rede.

</details>
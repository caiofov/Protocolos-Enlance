# Protocolos básicos de enlace de dados
<p>Protocolos básicos de enlance de dados implementados em Python. São eles:</p>
<br>

## Simplex sem restrições
<p>É o protocolo mais simples possível: não se preocupa com a possibilidade de algo sair errado, os dados são transmitidos em apenas um sentido, as camadas de rede do transmissor e do receptor estão sempre prontas, o tempo de processamento é ignorado, o espaço disponível do buffer é infinito e o canal de comunicação nunca é danificado ou perde dados.
Consiste em dois procedimentos distintos: um que envia informações (Sender) e outro que recebe (Receiver)</p>

## Stop and wait em canal livre de erros
<p>Este protocolo impede que o Sender sobrecarregue o Receiver, pois, para enviar o próximo quadro, necessita de uma confirmação. É considerado em um canal livre de erros, ou seja, nenhum quadro será perdido.</p>

## Stop and wait em canal com ruído
<p><É o único protocolo básico que considera erros. Funciona da mesma forma que o anterior (com quadros de confirmação), mas com a diferença que os quadros agora podem ser perdidos. Para fazer esse controle, é necessário o uso de um timer no Sender e também o armazenamento das sequências dos quadros, tanto no Sender quanto no Receiver/p>

<br>
> <b>Referência:</b> Redes de Computadores - Tanembau e Wetherall - 5ª edição

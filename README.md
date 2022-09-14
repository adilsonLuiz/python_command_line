# createArray

Este é um utilitario pare ser consumido por um terminal, por tanto, você precisa colocar o arquivo fonte no PATH do seu sistema operacional para poder executar de qualquer diretorio.
O objetivo do createArray é gerar um array a partir de uma fonte de dados do tipo string.

um exemplo 'DADOS, DADOS, DADOS', seria uma fonte de dados valida para ser trasnformado em um array.


# Parametros disponiveis

#--break
Se este parametro for utilizado ira "quebrar" a geração do array colocando dentro de cada array a quantidade de elementos igual ao valor deste paramentro
EX: createArray --break 2 'DADOS, DADOS, DADOS, DADOS' 
Output: Array01: ['DADOS', 'DADOS'], Array02: ['DADOS', 'DADOS']




Ex de uso:

Python CreateArray.py --break 2 'element1, element2, element3, element4'

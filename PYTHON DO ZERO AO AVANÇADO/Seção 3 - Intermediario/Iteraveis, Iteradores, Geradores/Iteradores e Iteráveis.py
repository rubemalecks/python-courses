# Iteraveis, Iteradores

# ~ ITERADORES:

"""
Um objeto que representa um fluxo de dados. Repetidas chamadas ao método
__next__() de um iterador (ou passando o objeto para a função embutida next())
vão retornar itens sucessivos do fluxo. Quando não houver mais dados disponíveis
uma exceção StopIteration exception será levantada. Neste ponto, o objeto
iterador se esgotou e quaisquer chamadas subsequentes a seu método __next__()
vão apenas levantar a exceção StopIteration novamente. Iteradores precisam ter
um método __iter__() que retorne o objeto iterador em si, de forma que todo
iterador também é iterável e pode ser usado na maioria dos lugares em que um
iterável é requerido. Uma notável exceção é código que tenta realizar passagens
em múltiplas iterações. Um objeto contêiner (como uma list) produz um novo
iterador a cada vez que você passá-lo para a função iter() ou utilizá-lo em um
laço for. Tentar isso com o mesmo iterador apenas iria retornar o mesmo objeto
iterador esgotado já utilizado na iteração anterior, como se fosse um contêiner
vazio.

[resumo] Sempre vai retornar um valor de cada vez"""


# ~ ITERÁVEIS:

"""
Um objeto capaz de retornar seus membros um de cada vez. Exemplos de iteráveis
incluem todos os tipos de sequência (tais como list, str e tuple) e alguns tipos
não sequenciais como dict, objeto arquivo, e objetos de qualquer classe que você
definir com um método __iter__() ou com um método __getitem__() que implemente a
semântica de Sequencia.

Iteráveis podem ser usados em um laço for e em vários outros lugares em que uma
sequência é necessária (zip(), map(), …). Quando um objeto iterável é passado
como argumento para a função nativa iter(), ela retorna um iterador para o
objeto. Este iterador é adequado para se varrer todo o conjunto de valores. Ao
usar iteráveis, normalmente não é necessário chamar iter() ou lidar com os
objetos iteradores em si. A instrução for faz isso automaticamente para você,
criando uma variável temporária para armazenar o iterador durante a execução do
laço.

[resumo] É um objeto que podemos iterar sobre ele mas ele não é necessariamente
um iterador. Em resumo ele não vai retornar um valor de cada vez."""


"""
lista = list(range(0, 8))
print(lista)
print(hasattr(lista, "__iter__"))"""


"""~ lista é um iterável"""

"""print(hasattr(lista, "__next__"))"""

"""~ lista NÃO é um iterador"""

import sys

l1 = [x for x in range(10000)]  # listcomprehension
l2 = (x for x in range(10000))  # Gerador

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))

# Mesmo que aumente os valores o gerador permanece ocupando a mesma quantidade
# de memoria

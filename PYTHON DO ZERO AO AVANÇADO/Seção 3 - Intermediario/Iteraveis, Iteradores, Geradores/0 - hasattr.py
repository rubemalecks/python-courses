"""
hasattr() é uma função de utilitário embutida em Python que é usada em muitos
aplicativos de programação do dia-a-dia. Sua principal tarefa é verificar se um
objeto tem o atributo nomeado fornecido e retornar verdadeiro se presente, caso
contrário, falso.

Sintaxe: hasattr (obj, chave)

Parâmetros: obj: O objeto cujo atributo deve ser verificado. chave: Atributo que
precisa ser verificado.

Retorna: Retorna True, se o atributo estiver presente, senão retorna False.
____________________________________________________________________________
[resumo] O método hasattr() retorna verdadeiro se um objeto tiver o atributo
nomeado dado e falso se não o fizer.
---------------------------------------------
hasattr() método leva dois parâmetros:

OBJETO - objeto cujo atributo nomeado deve ser verificado...
em python tudo é um objeto!
ATRIBUTO - nome do atributo a ser pesquisado
------------------------------------
"""


class Pessoa:
    idade = 23
    nome = "Jim Happer"


dado = Pessoa()

print("Pessoa tem idade?:", hasattr(dado, "idade"))  # o objeto tem o atributo 'idade'
print("Pessoa tem nome?:", hasattr(dado, "nome"))  # o objeto tem o atributo 'nome'
print("Pessoa tem nome?:", hasattr(dado, "nasc"))  # o objeto tem o atributo 'nasc'


# Podemos usar também dessa forma:

lista = list(range(3))
print(hasattr(lista, "__iter__"))  # lista = 'objeto',"__iter__" = 'atributo' pesquisado

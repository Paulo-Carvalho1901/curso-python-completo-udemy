"""
Lista python
Tipo list - mutável
suporta vários valores de quaquer tipo 
conhecemento reutilizaveis - indices e fatiamentos metodos úteis
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove ao final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena itens
Creat Read Update Delete
Criar, ler, alterar, apagar = lista[1] (CRUD)

"""
#        0   1   2   3    - Índices da lista
lista = [10, 20, 30, 40]
lista.append('Paulo') # Inserindo um item na utlma posição da lista
nome = lista.pop() # Removendo o ultimo item da lista e atribuindo a variável nome
lista.append(1233)
del lista[-1] # deletando o utimo valor
# lista.clear()
lista.insert(100, 5)
print(lista)

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

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_c)
print(lista_a)
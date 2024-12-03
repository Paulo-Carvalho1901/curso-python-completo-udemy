"""
Lista python
Tipo list - mutável
suporta vários valores de quaquer tipo 
conhecemento reutilizaveis - indices e fatiamentos metodos úteis
    append, insert, pop, del, clear, extend, +
Create Read Update Delete
Creia, ler, alterar, apagar = lsiat[1] (GRUD) 

"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

lista.append(50) # adicionando um item na lista com 'append'
lista.pop() # pop utilizado para remover o ultimo valor de uma lista
lista.append(60) 
lista.append(70)
utimo_valor = lista.pop(3)
print(lista, 'Removido', utimo_valor)
"""
Exercício
Exbiba os Índice da lista

"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

indices = range(len(lista))

for indece in indices:
    print(indece, lista[indece], type(lista[indece]))


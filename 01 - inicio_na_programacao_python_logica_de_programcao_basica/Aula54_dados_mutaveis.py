"""
Cuidados com dados mútaveis
= - copiados o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# nome = 'Paulo'
# mostra_variavel =  nome
# nome = 'João'
# print(nome)
# print(mostra_variavel)

lista_a = ['Paulo', 'Andreia', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
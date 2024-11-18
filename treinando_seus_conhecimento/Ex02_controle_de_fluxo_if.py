# Exercicios de estrutura condicional - if

# nome = 'Paulo'

# if nome == 'Paulo':
#     print('É Paulo')


# if 'Paulo' in lista:
#     print('sim')

# if variavel1 is True:
#     print('Sim')

# if e else

# if variavel1 == 'Paulo':
#     print('Sim, é igual')

# else:
#     print('Não é igual')
# print('Pulou direto')

#elif 
# Declaração das variaveis
# variavel1 = ('Paulo')
# variavel2 = 33


# código em if, elif e else
# if variavel1 == 'Paulo':
#     print('É o Paulo')

# elif variavel1 == 'Davi':
#     print('É o Davi')

# elif variavel1 == 'Andreia':
#     print('É a Andreia')

# else:
#     print('Não é O Paulo nem o Davi nem a Andreia')

# print('Pulou direto')

# lista = ['Paulo', 'Berlinga', 'Davi', 'Daniel']

# for nome in lista:
#     if nome == 'Paulo':
#         print('E o Paulo')
#     else:
#         print('Não o Paulo')

ordens = ['2001012', '3030304050', '40005004305', '20067802', '3030356750', '40005005675', '3939304050', '24505004305', '30076800']

for ordem in ordens:
    if ordem[0] == '2':
        print(f'A ordem {ordem} é uma manutenção preventiva')
    elif ordem[0] == '3':
        print(f'A ordem {ordem} é uma manutenção Corretiva')
    else:
        print(f'A ordem {ordem} é uma manutenção Preditiva')
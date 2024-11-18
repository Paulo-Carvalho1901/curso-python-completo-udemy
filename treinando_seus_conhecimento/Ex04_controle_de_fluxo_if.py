# EXERCICIO META DE VENDAS

"""
1) Você precisa criar um programa que calcule o bunus dos 
funcionários de sua empressa.A meta de vendas é de 500 reais, 
se um funcionário vendeu igual ou mais do que a meta,
ele ganha 50 reais de bÔnus, se não, ele nçao ganha bÔnus
"""
"""
se as vendas forem maior ou iguais a meta
    -então ganha bÔnus de 50
caso contrário 
    -Não ganha o bÔnus 

"""

# meta = 500
# venda = 501

# if venda >= meta:
#     print('Parabéns ganhou o bÔnus! ')
#     print('Enviar e-mail para funcionario.')
# else:
#     print('Infelismente não atingiu a meta.')

"""
2) Sua empresa resolveu valorizar funcionários que vendem
MUITO. Agora, existe uma super meta de vendas, que é de
1500 reais, se o funcionario vendeu igual ou mais que a
super meta, ele ganha 100 reais de bônus. Se ele vendeu igual
ou mais que a meta, (500 reais), ele ganha 50 de bônus se não
bateu a meta ele não ganha bônus
"""

meta = 500
super_meta = 1500
venda = 800
if venda >= super_meta:
    print('Parabéns você ganhou um bônus de 100 reais')
elif venda >= meta:
    print('Parabéns você ganhou um bônus de 50 reais')
else:
    print('Voce não atingiu a meta')

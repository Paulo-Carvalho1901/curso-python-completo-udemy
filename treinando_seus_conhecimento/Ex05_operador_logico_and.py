# Operador lógico AND (E)

"""
No caso do operador lógico (AND) só sera verdadeiro quando as suas ações forem verdadeiras caso uma das suas seja falsa, todas serem falsas

#VERDADEIRA E #VERDADEIRA
comparação1 and comparação2

RETORNA == VERDADE

"""
while True:
    nome = input('QUal é sua nome?' )
    idade = input('Qual é sua idade? ')

    idade = int(idade)

    #Limite para pegar emprestimo
    idade_menor = 20
    idade_maxima = 30 

    if idade >= idade_menor and idade <= idade_maxima:
        print(f'{nome} pode pagar o emprestimo. ')
    else:
        print(f'{nome} Não pode pagar o emprestimo. ')
#importando modulo
import os

# Variaveis para progama funcionar
palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ').strip()
    numero_tentativas += 1

    # Validando se usuário digitou apenas 1 letra
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    # Verificando se a letra digitada está na palvra secreta
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta 
        else:
            palavra_formada += '*'

    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU PARABÉNS!')
        print('A palavra éra', palavra_secreta)
        print('Tentativas: ', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
        
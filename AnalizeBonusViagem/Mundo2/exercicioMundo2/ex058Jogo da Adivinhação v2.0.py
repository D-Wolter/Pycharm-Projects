# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

# from random import randint
# from time import sleep
# computador = randint(0,6)
# user = int(input('digite um numero'))
# while user != computador:
#     user = int(input('voce ainda nao acertou escolha outro numero'))
#
# print(computador)
#
# print('eu pensei no numero {} voce acertou'.format(computador))
#
#
#
#




from random import randint
computador = randint(0, 10)
print('adivinhe o numero de 0 a 10')

acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite?'))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('mais... tente outra vez')
        elif jogador > computador:
            print('menos... tente outa vez')
print("era o numero {} acertou com {} tententativas!".format(computador, palpites))








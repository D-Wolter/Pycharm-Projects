#crie um programa que faça o computador jogar jokenpô com voçe.
import random
geraN = random.randint(1,3)
jogador = int(input('escolha um numero \n'
                    '(1) para pedra \n'
                    '(2) para papel \n'
                    '(3) para tesoura'))
if jogador >= 4 or jogador <= 0:
    print('voce deve escolher um numero de 1 ate 3')

pedra = 1
papel = 2
tesoura = 3

if geraN == 1 and jogador == 3:
    print('o computador escolheu pedra e voce escolheu tesourao computador ganhou')
elif jogador == 3 and geraN == 1:
    print('o computador escolheu tesoura e voce escolheu pedra, voce me venceu')
elif geraN == 3 and jogador == 2:
    print('o computador escolheu a tesoura e voce escolheu o papel o computador venceu')
elif jogador == 3 and geraN == 2:
    print('o computador escolheu papel e voce escolheu tesoura voce me venceu')
elif geraN == 2 and jogador == 1:
    print('o computador escolheu papel e voce escolheu pedra, o computador venceu')
elif jogador == 2 and geraN == 1:
    print('o computador escolheu pedra e voce escolheu papel, voce me venceu')
elif jogador == geraN:
    print('empate jogue novamente')

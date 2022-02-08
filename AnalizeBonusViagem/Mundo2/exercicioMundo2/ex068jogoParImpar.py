# from random import randint
# print('-=' * 22)
# print('VAMOS JOGAR PAR OU ÍMPAR')
# print('-=' * 22)
# cont = 0
# while True:
#
#     pc = randint(0,10)
#     print(pc)
#     user = int(input('escolha um numero'))
#     PI = str(input('escolha PAR ou ÌMPAR [P/I]')).upper().strip()[0]
#     soma = user + pc
#     if PI in 'Pp' and soma % 2 == 0:
#         print('-=' * 22)
#         print(f'Voce jogou {user} e o computador {pc}. Total de {soma} deu PAR ')
#         print('-=' * 22)
#         print('Voce me Venceu!')
#         print('VAMOS JOGAR NOVAMENTE')
#         cont += 1
#     elif PI in 'Ii' and soma % 2 == 1:
#         print('-=' * 22)
#         print(f'Voce jogou {user} e o computador {pc}. Total de {soma} deu IMPAR ')
#         print('-=' * 22)
#         print('Voce me Venceu!')
#         print('VAMOS JOGAR NOVAMENTE')
#         cont += 1
#     else:
#
#
#         break
#
# print('voce perdeu')
# print('-=' * 22)
# print(f'Você venceu {cont} vezes.')

#cod prof
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valo: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('[P/I]')).strip().upper()[0]
    print(f'voce jogou {jogador} e o computador {computador}. dotal de {total}')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')
    if tipo =='P':
        if total % 2 == 0:
            print('voce venceu')
            v += 1
        else:
            print('voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('voce venceu')
            v += 1
        else:
            print('voce perdeu')
            break
    print('vamos joagar novamente')
print(f'Game Over! voce venceu {v} vezes.')
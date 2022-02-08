# from random import  randint
# jogo = []
# totjogo = []
# cont = 0
# user = int(input('quantos jogos gostaria de gerar?'))
# for b in range(1, user+1):
#     for a in range(1, 7):
#         jogos = (randint(1, 61))
#         if jogos not in jogo:
#             jogos = (randint(1, 61))
#         jogo.append(jogos)
#     cont += 1
#     print(f'Jogo {cont} {jogo}')
#     totjogo.append(jogo[:])
#     jogo.clear()
# print('-=' * 30)



#cod prof
from random import randint
from time import sleep
lista = []
jogos = []
print('-=' * 30)
print('       JOGA NA MEGASENA        ')
print('-=' * 30)
quant = int(input('quantos jogos quer que seja gerado?'))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE >', '-=' * 5)
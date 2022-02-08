from random import randint
from operator import itemgetter
from time import sleep
jogo = {'jogador1': randint(1,6),'jogador2': randint(1,6),'jogador3': randint(1,6),'jogador4': randint(1,6)}
vencedores = []
print('Valores Sorteados:')
for i, k in jogo.items():
    print(f'O {i} com {k}')
    sleep(1)
print('-=' * 20)
vencedores = sorted(jogo.items(), key=itemgetter(1), reverse=True)
#key=itemgetter(1) escolhe por qual indice ordenar, depois poe em ordem decrescente com reverse=true
print('-=' * 20)
print(' ===  RANQUIM JOGADORES  ===  ')
for i, v in enumerate(vencedores):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
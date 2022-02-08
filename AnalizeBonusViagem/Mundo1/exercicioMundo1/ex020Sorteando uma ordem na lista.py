# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que
# leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

import random

lista = ['DANI', 'JOAO', 'LUANA', 'TIGO']
nfunc = len(lista)
sorteado = random.sample(lista)
print(nfunc)
'''

# repetidos = []
# sorteado = []
# while
#     repetidos = random.sample(lista)
#     if sorteado not in repetidos:
#         repetidos.append(sorteado)

from random import shuffle
n1 = str(input('digite o primeiro nome'))
n2 = str(input('digite o segundo nome'))
n3 = str(input('digite o terceiro nome'))
n4 = str(input('digite o quarto nome'))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('a ordem de apesentaçao sera')
print(lista)
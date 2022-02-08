'''#o computador gera um numero  inteiro de 0 a 5 peça ao usuario tentar  se adivinha recebe uma mensagem
import random
numero = random.randint(0,5)
print(numero)
escolha = int(input('escolha um numero de 0 a 5'))
print('voce acertou' if numero == escolha else 'voce erro')
'''
#prof cod
from random import randint
from time import sleep
computador = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente Advinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu penssei?'))
print('Processando')
sleep(3)
if jogador == computador:
    print('Parabens! Voçe conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))
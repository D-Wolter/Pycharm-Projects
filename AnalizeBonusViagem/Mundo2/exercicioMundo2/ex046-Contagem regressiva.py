'''
import time
n = 11
for cont in range(1, 11):
    n = n-1
    print('contagem regressiva {}!'.format(n))
    time.sleep(1)
print('Feliz Ano Novo')
'''
#cod prof
from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('feliz ano novo')
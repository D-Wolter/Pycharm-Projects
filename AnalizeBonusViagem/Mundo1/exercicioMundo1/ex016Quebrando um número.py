#crie um programa que leia um numero real 6.127 e mostre porçao inteira 6
from math import trunc, floor
real = 6.678
print(floor(real))

#cod prof
num = float(input('digite um numero'))
print('o vlor digitado foi {} e a sua porcao inteira é {}'.format(num, trunc(num)))


#prof cod2
num2 = float(input('digite um valor'))
print('o valor digitado foi {} e a sua porcao inteira e {}'.format(num2, int(num2)))


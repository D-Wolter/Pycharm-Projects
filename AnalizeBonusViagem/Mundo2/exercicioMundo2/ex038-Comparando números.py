#escreva um programa que leia dois numeros inteiros e compareos, mostrando qual o valor maior, menor e se sao iguais.

num1 = int(input('escolha o primero numero'))
num2 = int(input('escolha osegundo numero'))

maior = num1
if num2 > num1:
    print('o valor indicado foi {} e {}, o segundo valor foi o maior'.format(num1, num2))
elif num2 == num1:
    print('o valor indicado foi {} e {}, os dois valores sao iguais'.format(num1, num2))
else:
    print('ovalor indicado foi {} e {}, o primeiro valor e maior'.format(num1, num2))
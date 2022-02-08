#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
# #prof cod

co = float(input('Comprimento do cateto oposto:'))
ca =float(input('comprimento do cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
#modulo math de calculo de hipotenusa
from math import hypot
hy = hypot(co, ca)
print('hipotrnusa vai medir {:.2f}'.format(hy))



#calcular se a medida de tres retas podem formar um triagulo
print('-=-' * 20)
print('Anaizador de triangulos')
print('-=-' * 20)
r1 = float(input('primeiro segmento'))
r2 = float(input('segundo segmento'))
r3 = float(input('terceiro segmernto'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3< r1 + r2:
    print('os segmentos podem formar um triangulo')
else:
    print('os segmentos nao podem formar um triangulo')

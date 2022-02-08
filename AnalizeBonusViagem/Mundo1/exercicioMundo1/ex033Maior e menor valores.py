#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('digite um numero'))
b = int(input('digite outro numero'))
c = int(input('digite mais outro numero'))
#verificar menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c


#verificar maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c


print('o menor valor foi {}'.format(menor))
print('omaior valoe foi {}'.format(maior))
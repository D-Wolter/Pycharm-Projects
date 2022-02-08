#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

dataatual = 2022
menor = 0
maior = 0
for c in range(1,8):
    ano = int(input('digite o ano do seu nascimento'))
    if dataatual - ano < 18:
        menor = menor+1
    elif dataatual - ano >= 18:
        maior = maior+1
print('das sete pessoas temos {} menores de idade e {} maiores de idade'.format(menor, maior))

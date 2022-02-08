#faça um programa que leia o nao de nascimento de um cidadao e informe a ele, quanto tempo falta, se esta na data, se tem de esperar
import datetime
ano = int(input('digite o ano do seu nascimento ex 1999 '))

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
print(f"Current Year -> {year}")
dataAtual = int(year)

idade =  dataAtual - ano
espera = 18-idade
passou = idade-18
print(idade)
print(espera)
print(passou)
if idade < 18:
    print('ainda falta {} anos para seu alistamento'.format(espera))
elif idade == 18:
    print('Voce deve se apresentar esse ano ao exercito')
elif idade > 18:
    print('voce devia ter se apresentado a {} anos atraz, favor regularizar'.format(passou))
print('o exercito agradeçe seu comtato')
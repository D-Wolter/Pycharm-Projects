#a confederaçao de nataçao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de
#acordo com a idade.

#ate 9 anos MIRIM
#ate14 anos INFANTIL
#ate19 anos JUNIOR
#ate20 anos SENIOR
#acima MASTER

import datetime
ano = int(input('digite o ano do seu nascimento ex 1999 '))

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
print(f"Current Year -> {year}")
dataAtual = int(year)
idade = dataAtual - ano
print(idade)
if idade < 9:
    print('voce pode participar da categoria MIRIM ate 9 os anos')
elif idade > 9 and idade < 14:
    print('voce pode participar da categoria INFANTIL ate os 14 anos')
elif idade > 14 and idade < 19:
    print('voce pode participar da categoria JUNIOR ate os 19 anos')
elif idade == 20:
    print('voce pode participar da categoria SENIOR a partir do proximo ano sera master')
elif idade > 20:
    print('voce pode participar da categoria MASTER parabens')

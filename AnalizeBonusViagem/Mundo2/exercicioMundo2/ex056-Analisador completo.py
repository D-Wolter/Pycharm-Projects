# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
# grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# maisvelho = 'daniel'
# menor20 = 0
# idades = 0
# mediamenor = 0
# mediamaior = 0
# media = 0
# for c in range(1,5):
#     nome = str(input('digite seu nome'))
#     idade = int(input('digite sua idade'))
#     sexo = str(input('digite seu sexo M ou H'))
#     if idade < 20:
#         if sexo == 'M':
#             menor20 = menor20+1
#     if maisvelho == "daniel":
#         maisvelho = nome
#     if idades == 0:
#         idades = idade
#     if idade > idades and sexo =='H':
#         idades = idade
#         maisvelho = nome
#     if mediamaior == 0:
#         mediamaior = idade
#     if idade > mediamaior:
#         mediamaior = idade
#     if mediamenor == 0:
#         mediamenor = idade
#     if idade < mediamenor:
#         mediamenor = idade
#     media = mediamenor+((mediamaior - mediamenor) / 2)
# print('temos {} mulheres menores, o homen mais velho é sr {}, e a media de idade é {:1}.'.format(menor20, maisvelho, media))


#cod prof
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for p in range(1,5):
    print('---------{}ª PESSOA --------'.format(p))
    nome = str(input('Nome: '))
    idade =int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1

mediaidade = somaidade / 4
print('a media de ideda do grupo é de {} anos'.format(mediaidade))
print('o homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('sao {} mulheres com menos de 20 anos'.format(totmulher))

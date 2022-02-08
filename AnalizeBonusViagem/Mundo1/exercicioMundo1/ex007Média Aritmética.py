

#leia notas de uma aluno, calcule e mostre as medias
nota1 = 9.5
nota2 = 6.5
soma = []
if nota1>nota2:
    soma = nota1-nota2
    soma = soma/2
    print('sua média é {:.1f}!'.format(nota2+soma))

if nota2 > nota1:
    soma = nota2 - nota1
    soma = soma / 2
    print('sua média é {:.1f}!'.format(nota1 + soma))

if nota2==nota1:
    print('sua média é {:.1f}!'.format(nota2))

#prof cod

n1 =float(input('digite a primeirA  nota'))
n2 = float(input('digite a segunda nota'))
media = (n1 + n2) / 2
print('a mdeia entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, media))
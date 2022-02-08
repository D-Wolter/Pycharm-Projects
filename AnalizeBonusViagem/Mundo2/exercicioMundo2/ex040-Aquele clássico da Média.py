#crie um programa que leia duas notas de um aluno e calcule sua media atingida
#media abaixo de 5.0 reprovado
#media entre 5.0 e 6.9 recuperação
#media7.0 ou superior aprovado

nota1 = float(input('digite a primeira nota'))
nota2 = float(input('digite a segunda nota'))
dif = []

maior = nota1
menor = nota2

if nota2 > nota1:
    maior = nota2
    menor = nota1

dif = (maior - menor) /2
media = menor + dif

if media < 5.0:
    print('sua media foi de {} voçe foi reprovado'.format(media))
elif media >= 5.0 and media < 6.9:
    print('sua media foi de {} voçe entrou em recuperação'.format(media))
elif media > 7.0:
    print('sua media foi de {} voce esta aprovado'.format(media))
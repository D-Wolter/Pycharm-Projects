#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

sexo = str(input('Qual seu sexo [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('informe sexo sexo com M ou F')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))

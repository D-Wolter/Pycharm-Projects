
#
# while True:
#     maior = 0
#     homens = 0
#     menor = 0
#     print('Cadastro RH')
#     repet = 'S'
#     while repet in 'S':
#         idade = int(input('Digite a idade do funcionario'))
#         sex = str(input('digite o sexo [M/F]')).upper().strip()[0]
#         if idade >= 18:
#             maior += 1
#             repet = str(input('Deseja fazer novo cadastro [S/N]')).upper().strip()[0]
#         elif sex in 'M':
#             homens += 1
#             repet = str(input('Deseja fazer novo cadastro [S/N]')).upper().strip()[0]
#         elif sex in 'F':
#             if idade < 20:
#                 menor += 1
#                 repet = str(input('Deseja fazer novo cadastro [S/N]')).upper().strip()[0]
#         else:
#             repet = str(input('Deseja fazer novo cadastro [S/N]')).upper().strip()[0]
#     else:
#         print('somando dados')
#         break
# print(f'temos {maior} pessoas maior de 18, foram cadastrados {homens} Homens e temos {menor} mulheres menores de 20')
#


  #cod prof

tot18 = tothomens = totmulher20 = 0
while True:
    idade = int(input('Digite a idade do funcionario'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo [M/F]')).strip().upper()[0]



    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        tothomens += 1
    if sexo == 'F' and idade < 20:
        totmulher20 += 1




    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp =='N':
        break
print(f'total de pessoas com mais de 18 anos foi {tot18}')
print(f'total de homens foi {tothomens}')
print(f'total de mulheres com menos de 20 anos foi {totmulher20}')
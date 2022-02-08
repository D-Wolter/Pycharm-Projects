# alunos = []
# temp = []
# c = 0
# while True:
#     temp.append((input('Nome: ')))
#     temp.append((float(input('Nota 1:'))))
#     temp.append((float(input('Nota 2:'))))
#     media = (temp[1] + temp[2]) / 2
#     temp.append(media)
#     alunos.append(temp[:])
#     temp.clear()
#
#     resp = str(input('Quer continuar [S/N]'))
#     if resp not in 'sSnN':
#         resp = str(input('Quer continuar [S/N]'))
#     if resp in 'nN':
#         break
#     if resp in 'sS':
#         c += 1
# print('-=' * 30)
# print('No. NOME          MÉDIA')
# print('-' * 20)
# n = 0
# print(c)
# for cont in range(0, int(c)):
#     for aluno in alunos:
#         print(f'{n}    {aluno[0]}            {aluno[3]}')
#         n += 1

ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2:'))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('quer continuar s n'))
    if resp in 'nN':
        break
print('-=' * 30)
print(f'{"No.":>4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 30)
for i , a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    opc = int(input(f'ver detalhes das notas de ulgum aluno?, (999 interrompe):'))
    if opc == 999:
        print('finalizado')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')
print('volte sempre')



# alunos = []
# aluno = {}
# aluno['nome'] = str(input('Nome: '))
# aluno['media'] = float(input(f'Media de {aluno["nome"]} '))
# alunos.append(aluno.copy())
# print(f'Nome é igual a {aluno["nome"]}')
# print(f'Média é igual a {aluno["media"]}')
# if aluno['media'] < 7.0:
#     print('Situação é igual a Reprovado')
# elif aluno['media'] >= 7.0:
#     print('Situação igual a Aprovado')
#

#cod prof
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situaçao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situaçao'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')


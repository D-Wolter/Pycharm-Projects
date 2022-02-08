lista = []
temp = {}
media = []
gmedia = 0

while True:
    temp['nome'] = str(input('Nome: '))
    sex = str(input('Sexo: [M/F]')).upper()[0]
    if sex not in 'mMfF':
        sex = str(input('deve digitar [M/F]')).upper()[0]

    temp['sexo'] = sex
    temp['idade'] = int(input('Idade: '))
    media.append(temp['idade'])
    lista.append(temp.copy())
    user = str(input('Quer continuar [S/N]')).upper()[0]
    if user not in 'sSnN':
        user = str(input('deve digitar [S/N]')).upper()[0]
    if user in 'nN':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(lista)} Pessoas Cadastradas.')
for v in media:
    gmedia += v
gmedia = gmedia / len(lista)
print(f'B) A média de idade é de {gmedia:.2f} anos.')
print(f'C) As mulheres cadatradas foram ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f' {p["nome"]}', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= gmedia:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}, ', end='')
            print()
print('<< ENCERRADO >>')









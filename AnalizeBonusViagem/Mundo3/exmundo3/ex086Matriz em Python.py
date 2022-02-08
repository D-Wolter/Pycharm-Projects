#
# tabela = []
#
# for n in range(0,3):
#    tabela.append(int(input(f'digite um valor para [0, {n}: ')))
# for n in range(0, 3):
#     tabela.append(int(input(f'digite um valor para [1, {n}: ')))
# for n in range(0, 3):
#     tabela.append(int(input(f'digite um valor para [2, {n}: ')))
#
# print('-=' * 30)
# print(f'\n [ {tabela[0]} ][ {tabela[1]} ][ {tabela[2]} ]\n [ {tabela[3]} ][ {tabela[4]} ][ {tabela[5]} ]\n [ {tabela[6]} ][ {tabela[7]} ][ {tabela[8]} ]')

#cod prof
matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'digite um valor para linha {l+1} coluna {c+1}: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')#:^5 centralizou o resultado com cinco enpaços
    print()#printa a quebra de linha a cada volta do laço
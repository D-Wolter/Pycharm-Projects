print('Gerador de P.A.')
print('-=' * 10)
primeiro = int(input('digite o primeiro termo'))
razao = int(input('razão da PA'))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ¬ '.format(termo), end='')
    termo += razao
    cont += 1

print('FIM')

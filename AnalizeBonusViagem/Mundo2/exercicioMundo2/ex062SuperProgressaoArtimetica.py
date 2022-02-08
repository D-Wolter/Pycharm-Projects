print('Gerador de P.A.')
print('-=' * 10)
primeiro = int(input('digite o primeiro termo'))
razao = int(input('razão da PA'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} ¬ '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('digite quatos termos gotaria dever a mais ou 0 para sair'))
print('progressao finalizada com {} termos mostrados.'.format(total))

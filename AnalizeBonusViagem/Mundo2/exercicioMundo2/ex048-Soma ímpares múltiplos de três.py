
soma = 0
for c in range(1,500):
    if c % 2 == 1:
        if c % 3 == 0:
            soma = soma+c
print('a soma dos numeros é {}'.format(soma))

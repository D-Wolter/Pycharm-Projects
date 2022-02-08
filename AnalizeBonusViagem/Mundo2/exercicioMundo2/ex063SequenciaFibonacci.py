print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
N = int(input('digite um numero para ver a sequencia fibonacci'))
t1 = 0
t2 = 1
print('-'*30)
print('{} ¬ {}'.format(t1, t2), end='')
cont = 3
while cont <= N:
    t3 = t1 + t2
    print(' ¬ {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' ¬ Fim')
print('-'*30)
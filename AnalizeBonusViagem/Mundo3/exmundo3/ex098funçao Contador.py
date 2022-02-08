from time import sleep

def lin():
    print('=' * 30)

def PA(ini, fim, raz):
    print(f'Contagem de {ini} até {fim} de {raz} em {raz}')
    lin()
    if raz > 0:
        for c in range(ini+1, fim+1, raz):
            print(f'{c} ', end='')
            sleep(0.5)
        print('FIM')
    if raz < 0:
        for c in range(ini, fim - 1, raz):
            print(f'{c} ', end='')
            sleep(0.5)
        print('FIM')
    print()
    lin()

PA(0, 10, 1)
PA(10, 0, -2)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim =  int(input('Fim: '))
passo =  int(input('Passo: '))
PA(inicio, fim, passo)
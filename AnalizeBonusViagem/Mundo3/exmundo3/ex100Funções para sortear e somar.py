from random import  randint
def gerador():
    soma = 0
    lista = [randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), ]
    print(f'Sorteamos 5 valores da lista: ', end='')
    for v in lista:
        print(f'{v} ',end='')
        if v % 2 == 0:
            soma += v
    print('PRONTO!')
    print(f'Somando os valores pares de {lista} temos {soma}')

gerador()

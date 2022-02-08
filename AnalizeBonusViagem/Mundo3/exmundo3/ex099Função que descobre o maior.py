from  random import randint

def lin():
    print('-=' * 30)

def gerador(*num):
    pos = 0
    lin()
    pos += 1
    print('Analizando valores passados...')
    for v in num:
        print(f'{v} ',end='')
    print(f'foram encontrados {len(num)} ao todo.')
    print(f'O maior valor informado foi {max(num)}')

gerador(6, 3, 9, 1, 0, 2)
gerador(4, 7, 0)
gerador(1, 2)
gerador(6)
gerador()


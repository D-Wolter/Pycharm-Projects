while True:
    print('-=' * 26)
    n = int(input('escolha um numero posiotivo para ver a tabuada ?  '))
    print('-=' * 26)
    cont = 0
    if n < 0:
        break
    while cont < 10:
        cont += 1
        soma = n * cont

        print(f'{n}  x  {cont}  =  {soma}')
print('finalizado')
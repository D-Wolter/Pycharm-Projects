n = s = 0
cont = 0
while True:
    n = int(input('digite um numero'))
    if n == 999:
        break
    cont += 1
    s += n
print(f'voce digitou {cont} numeros a soma vale {s}')
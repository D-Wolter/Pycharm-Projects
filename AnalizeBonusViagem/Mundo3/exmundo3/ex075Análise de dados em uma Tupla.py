

#cod prof
num = (int(input('digite un numero: ')),
       int(input('digite outro numero: ')),
       int(input('digite mais um numero ')),
       int(input('digite o ultimo numero ')))
print(f'Voce digitou os valores {num}')
print(f'o valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o primeiro 3 APARECEU NA POSICAO {num.index(3)+1}')
else:
    print('o valor trez nao foi declarado nenhuma vez')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
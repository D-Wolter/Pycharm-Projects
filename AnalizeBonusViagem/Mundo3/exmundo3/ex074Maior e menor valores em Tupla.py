#
# from random import randint
# numeros = []
# cont = 0
# maior = 1
# menor = 99
# while cont <= 4:
#     cont += 1
#     gerar = randint(1,99)
#     print(gerar)
#     if gerar < menor:
#         menor = gerar
#     elif gerar > maior:
#         maior = gerar
#     gerar = str(gerar)
#     numeros.append(gerar)
# print(numeros)
# print(f'o Maior valor gerado foi {maior} e o menor valor gerado foi o {menor}.')


from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end= '')
for n in numeros:
    print(f'{n} ', end='')


print(f'\n'
      f'O MAIOR VALOR FOI {max(numeros)}')
print(f'O Menor VALOR FOI {min(numeros)}')

# valores = []
# resp = 's'
# while resp in 'sS':
#     valor = int(input('Digite um valor: '))
#     if valor not in valores:
#         valores.append(valor)
#     else:
#         print('valor duplicado nao foi adicionado')
#     print('valor adiciona com sucesso...')
#     resp = str(input('Quer Continuar [S/N]'))
#     if resp not in 'sSnN':
#         resp = str(input('Quer Continuar [S/N]'))
#     if resp in 'nN':
#         break
#
#
# print(f'voce digitou os valores {valores}')




#cod Prof
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('valor adicionado sucesso')
    else:
        print('valor duplicado')
    r = str(input('quer continuar [S/N]'))
    if r in 'nN':
        break
print('-=' * 30)
numeros.sort()
print(f'voce digitou os valores {numeros}')
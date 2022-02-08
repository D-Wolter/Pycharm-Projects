n1 = int(input('primeiro valor'))
n2 = int(input('segundo valor'))
opcao = 0
while opcao != 5:
    print('''
    [1]somar     
    [2]multiplicar
    [3]maior
    [4]novos numeros
    [5]sair do programa''')
    opcao =int(input('qual a sua opcao'))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif opcao == 2:
        multi = n1 * n2
        print('A multiplicaçao entre {} e {} é {}.'.format(n1, n2, multi))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
    elif opcao == 4:
        print('Informe os numeros Novamente')
        n1 = int(input('primeiro valor'))
        n2 = int(input('segundo valor'))
    elif opcao == 5:
        print('Finalizando')
    else:
        print('opcao invalida')
    print('=-=' * 10)



print('Fim do programa')
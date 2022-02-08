# def leiaint(n):
#     ok  = 1
#     while ok != 0:
#         if n in '0987654321':
#             ok = 0
#             return print(f'o numero escolhido foi {n}')
#         elif n not in '0987654321':
#             return  leiaint(input('vc deve digita um nuero'))
# numero = input('digite un muero')
# leiaint(numero)
#


#cod prof

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero inteiro valido.\033[m')
        if ok:
            break
    return valor


#programa principal
n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
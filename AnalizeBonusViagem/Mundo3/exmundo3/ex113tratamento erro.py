def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um numero inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mentrada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um numero real valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mentrada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um numero: ')
n2 = leiafloat('Digite um numero real')
print(f'o valor digitado foi {n1} e o numero real foi {n2}')
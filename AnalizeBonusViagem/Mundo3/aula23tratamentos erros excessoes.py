try:#operaçao
    a = int(input('numerador: '))
    b = int(input('denominador: '))
    r = a / b
except:#falhou
    print('infelismente tivemos um erro :(')
else:#deu certo
    print(f'o resultado é {r:.1f}')
finally:#dando certo ou errado
    print('volte sempre')




try:
    a = int(input('numerador: '))
    b = int(input('denominador: '))
    r = a / b
except Exception as erro:
    print(f'infelismente tivemos um erro {erro.__class__}')
else:
    print(f'o resultado é {r:.1f}')
finally:
    print('volte sempre')




try:
    a = int(input('numerador: '))
    b = int(input('denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('tivemos um problema com os tipos de dadeos quev digitou')
except ZeroDivisionError:
    print('nao é possivel dividir um numero por 0')
except KeyboardInterrupt:
    print('o usuario preferil nao informar os dados')
except Exception as erro:
    print(f'o erro encontrado foi {erro.__cause__}')
else:
    print(f'o resultado é {r:.1f}')
finally:
    print('volte sempre')
nums = ('zero', 'um', 'dois', ' trez', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
        'treze', 'quatorsze', 'quinze', 'dezeseis' 'dexesete', 'dezoito', 'dezenove', 'vinte')

while True:
    user = int(input('digite um numero de 0 ate 20'))
    if 0 <= user <= 20:
        break
    print('Tente novamente. ', end='')

print(f'voce digitou um numero {nums[user]}')

resta = input(str('Voce deseja continuar [S/N]')).upper()


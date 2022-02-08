#escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolhr qua sera a base de conversao:

#-1 para binario
#-2 para octal
#3 para hexadecimal

num = int(input('digite um numero inteiro'))

base = int(input('escilha um numero para conversao \n'
                 '(1) BINARIO \n'
                 '(2) octal \n'
                 '(3) hexadecimal'))


binario = format(num, 'b')
octal = format(num, 'o')
hexadecimal = format(num, 'x')

if base == 1:
    print('o valor decimal {}, corresponde ao valor binario {}!'.format(num, binario))
elif base == 2:
    print('o valor decimal {} corresponde ao valor octal {}!'.format(num, octal))
elif base == 3:
    print('o valor decimal {} corresponde ao valor hexadecimal {}!'.format(num, hexadecimal))
else:
    print('precisa escolher um numero entre 1 a 3!')
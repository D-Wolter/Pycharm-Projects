# num = int(input('digite um numero primo'))
#
# nmb = 0
# for c in range(2, num):
#     if num % c == 0:
#         nmb = nmb+1
#
# if nmb == 0:
#     print('primo')
# elif nmb > 0:
#     print('nao é primo')
#
#



#cod prof
num = int(input('digitre um numero'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')
print('\033[mO Numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('e por isso é um numero primo')
else:
    print('e por isso ele não é primo')
termo = int(input('digite o primeiro termo'))
razao = int(input('digite a razão'))
ran = 0
for c in range(0,10):
    ran = ran+1
    print('O termo {:2} é {}.'.format(ran,termo))
    termo = termo+razao


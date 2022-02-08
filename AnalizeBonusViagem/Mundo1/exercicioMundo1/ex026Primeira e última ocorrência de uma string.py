

#leia uma frase e mostre quantas vezes aparecea letra A,em que posicao aparece a primeira vez, em que posicao
# aparece pela ultima vez
ffrase = str(input('Digite uma frase')).upper().strip()
print('a letra A aparece {} vezes na frase'.format(ffrase.count('A')))
print('a primeira letra A aperece na posicao {}'.format(ffrase.find('A')+1))
print('a ultima letra A aparece na posicao {}'.format(ffrase.rfind('A')+1))

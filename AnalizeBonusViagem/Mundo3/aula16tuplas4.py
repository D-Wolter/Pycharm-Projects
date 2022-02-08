
lanche = ('Hambúrger', 'suco', 'pizza', 'pudim', 'batata frita')#PODESER ECRITA SEM COLCHETES


#checar posiçao range
for cont in range(0, len(lanche)):
    print(f'eu vou ingerir {lanche[cont]} na posição {cont}')
#listar começando range 0
for pos, comida in enumerate(lanche):
    print(f'eu vou traçar {pos}, {comida}')
#listar produto começaodo por 1
for pos, comida in enumerate(lanche):
    print(f'eu vou traçar {pos+1}, {comida}')
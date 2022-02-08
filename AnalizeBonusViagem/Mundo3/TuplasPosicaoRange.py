lanche = ('Hambúrger', 'suco', 'pizza', 'pudim', 'batata frita')#PODESER ECRITA SEM COLCHETES
for comida in lanche:
    print(f'Eu vou comer {comida}')
# Eu vou comer Hambúrger
# Eu vou comer suco
# Eu vou comer pizza
# Eu vou comer pudim
# Eu vou comer batata frita
for cont in range(0, len(lanche)):
    print(f'na posiçao {cont} para comer {lanche[cont]}')
# na posiçao 0 para comer Hambúrger
# na posiçao 1 para comer suco
# na posiçao 2 para comer pizza
# na posiçao 3 para comer pudim
# na posiçao 4 para comer batata frita

for posicao, comida in enumerate(lanche):#funciona igual o anterior
    print(f'Eu vou comer {comida} na posicao {posicao}')
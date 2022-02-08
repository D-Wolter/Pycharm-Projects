from datetime import  datetime
valor = {}
lista = []
valor['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
valor['idade'] = datetime.now().year - nasc
ctps = int(input('Carteira de trabalho (0 não tem):'))
cart = ''
if ctps == 0:
    lista.append(valor.copy())
    cart = 0
else:
    valor['ctps'] = ctps
    valor['contrataçao'] = int(input('Ano da contrataçao'))
    valor['salario'] = str(input('Salário'))
lista.append(valor.copy())
print('-=' * 40)
print(valor)
print(f'o nome tem o valor {valor["nome"]}')
print(f'idade tem o valor {valor["idade"]}')
if cart ==0:
    print('Nao possui carteira de trabalho')
if "ctps" in valor:
    print(f'ctps tem o valor {valor["ctps"]}')
if "salario" in valor:
    print(f'salario tem o valor {valor["salario"]}')
if "contrataçao" in valor:
    pens = valor['contrataçao' ] - nasc + 35
    print(f'aposentadoria tem o valor {pens}')

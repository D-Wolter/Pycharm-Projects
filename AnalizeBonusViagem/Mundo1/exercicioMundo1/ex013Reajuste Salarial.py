
#CALCULAR AUMENTO
salario = 2000





salario = float(input('digite seu salario exemplo 2000'))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print('seu salario vai passar de {} reais paRA {} REAIS PARABENS'.format(salario, novo))
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores
# a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.




salario = int(input('digite o salario ex 1500'))
aumento10 = int(salario * 10 / 100)
aumento15 = int(salario * 15 / 100)

if salario <= 1250:

    print('Seu salario recebeu {:.2f} reais  de aumento e passou a ser de {:.2f} reais'.format(aumento10, salario+aumento10))
else:
    print('Seu salario recebeu {:.2f} reais de aumento e passou a ser de {:.2f} reais'.format(aumento15, salario+aumento15))
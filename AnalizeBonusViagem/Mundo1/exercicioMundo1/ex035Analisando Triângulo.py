r1 = float(input('digite o valor da primeira reta'))
r2 = float(input('digite o valor da segunda reta'))
r3 = float(input('diite o valor da terceira reta'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print("a reta 1 de {} a reta 2 de {} e a reta 3 de {} podem formar um triangulo")
else:
    print("a reta 1 de {} a reta 2 de {} e a reta 3 de {} NAO PODEM FORMAR TRIAGULO")

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

def area(c, l):
    a = c * l
    print(f'A area de um terreno {c} x {l} é de {a}m².' )

area(largura, comprimento)
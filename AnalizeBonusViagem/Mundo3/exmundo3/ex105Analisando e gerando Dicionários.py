

def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'boa'
        elif r['media'] >= 5:
            r['situação'] = 'razoavel'
        else:
            r['situação'] = 'ruim'
    return r






#programa principal
resp = notas(5.5, 9.5, 10, 6.5)
print(resp)
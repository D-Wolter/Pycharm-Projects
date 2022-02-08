def frases(*frase):
    for f in  frase:
        t = len(f) + 4
        print('=' * t)
        print(f'{f:^{t}}')
        print('=' * t)
frases('Daniel Wolter')
frases('Curso do Python Mundo3')
frases('DWM')




import time


def contagem(a, b, c):
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    print('-=' * 20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a < b:
        while a <= b:
            print(f'{a}', end=' ')
            a += c
            time.sleep(0.5)
        print('FIM')
    else:
        while a >= b:
            print(f'{a}', end=' ')
            a -= c
            time.sleep(0.5)
        print('FIM')


contagem(1, 10, 1)
contagem(10, 0, 2)
print()
print(f'-=' * 20)
print('Agora é sua vez de personalizar, informe inicio, fim e o passo: ')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))

contagem(a, b, c)

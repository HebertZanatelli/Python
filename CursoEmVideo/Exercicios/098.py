import time


def contagem(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    print('-=' * 20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    time.sleep(1.5)
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont}', end=' ')
            cont += c
            time.sleep(0.5)
        print('FIM')
    else:
        cont = a
        while cont >= b:
            print(f'{cont}', end=' ')
            cont -= c
            time.sleep(0.5)
        print('FIM')


contagem(1, 10, 1)
contagem(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))


contagem(a, b, c)


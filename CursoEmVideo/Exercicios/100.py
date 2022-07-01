import random

numeros = []

def sorteio(lista):

    c = 1
    while c <= 5:
        numero = random.randint(1, 10)
        lista.append(numero)
        c += 1
    print(f'Sorteando os {len(lista)} valores da lista: ', end='')
    for v in lista:
        print(v, end=' ')
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares da lista {lista}, temos {soma}')


sorteio(numeros)
somaPar(numeros)

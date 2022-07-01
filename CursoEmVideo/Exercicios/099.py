import time
import random

lista = []


def maior(*num):
    lista = []
    qtd = random.randint(0, 9)
    c = 0
    while c <= qtd:
        lista.append(random.randint(0, 10))
        c += 1
    print('-=' * 30)
    print(f'Analisando os Valores gerados...')
    time.sleep(0.5)
    for valor in lista:
        print(f'{valor}', end=' ')
        time.sleep(0.3)
    print(f'Foram informados {len(lista)} valores ao todo.')
    print(f'O maior valor informado é {sorted(lista)[-1]}')


maior(lista)
maior(lista)
maior(lista)
maior(lista)
maior(lista)

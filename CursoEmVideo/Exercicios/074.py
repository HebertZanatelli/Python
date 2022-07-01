import random
while True:

    tupla = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
             random.randint(0, 10), random.randint(0, 10))
    print(f'Os Valores sorteados para tupla foram:', end='')
    for n in tupla:
        print(f' {n} ', end=' ')
    print(f'\nO maior valor sorteado foi: {sorted(tupla)[-1]}')
    print(f'O menor valor sorteado foi: {sorted(tupla)[0]}')
    parar = input('Deseja continuar? [S/N] ').strip().upper()
    if parar == 'N':
        break
print('Fim de programa')

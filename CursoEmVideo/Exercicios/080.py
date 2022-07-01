lista = []
for c in range(5):
    n = int(input('Digite um numero para criar uma lista ordenada: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('O numero foi adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(lista)

matriz = [[], [], []]
for l in range(3):
    for c in range(3):
        matriz[l].append(int(input('Digite um numero')))
for l in range(3):
    for c in range(3):
        print(f'{matriz[l][c]:^4}',end='')
    print()
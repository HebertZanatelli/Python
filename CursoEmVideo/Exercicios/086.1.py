v = [[], [], []]
for c in range(3):
    v[0].append(int(input(f'Digite um valor para [0, {c}]: ')))
for c in range(3):
    v[1].append(int(input(f'Digite um valor para [1, {c}]: ')))
for c in range(3):
    v[2].append(int(input(f'Digite um valor para [2, {c}]: ')))
for c in range(3):
    print(f'[{v[0][c]:^5}]', end=' ')
print()
for c in range(3):
    print(f'[{v[1][c]:^5}]', end=' ')
print()
for c in range(3):
    print(f'[{v[2][c]:^5}]', end=' ')
print()


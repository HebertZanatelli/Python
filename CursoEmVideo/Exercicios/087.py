v = [[], [], [], []]
soma = soma_terceira = 0
for c in range(3):
    num = int(input(f'Digite um valor para [0, {c}]: '))
    if num % 2 == 0:
        v[3].append(num)
    v[0].append(num)
    if c == 2:
        soma_terceira += num
for c in range(3):
    num = int(input(f'Digite um valor para [1, {c}]: '))
    if num % 2 == 0:
        v[3].append(num)
    v[1].append(num)
    if c == 2:
        soma_terceira += num
for c in range(3):
    num = int(input(f'Digite um valor para [2, {c}]: '))
    if num % 2 == 0:
        v[3].append(num)
    v[2].append(num)
    if c == 2:
        soma_terceira += num
print('-='*30)
for c in range(3):
    print(f'[{v[0][c]:^5}]', end=' ')
print()
for c in range(3):
    print(f'[{v[1][c]:^5}]', end=' ')
print()
for c in range(3):
    print(f'[{v[2][c]:^5}]', end=' ')
print('-='*30)
for s in v[3]:
    soma += s
print(f'A soma dos numeros pares é: {soma}')
print(f'A soma dos valores da terceira coluna é {soma_terceira}')
print(f'O maior valor da segunda linha é {max(v[1])}')


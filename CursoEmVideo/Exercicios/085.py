lista = [[], []]
for c in range(7):
    num = int(input(f'Digite o {c+1}º valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print(f'Par: {sorted(lista[0])}')
print(f'Impar: {sorted(lista[1])}')
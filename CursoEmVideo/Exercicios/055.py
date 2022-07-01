lista = []
for c in range(1,6):
    peso = float(input(f'Informe o Peso da {c}ª pessoa: '))
    lista.append(peso)
lista.sort()
print(f'O maior peso inserido é: {lista[-1]}')
print(f'O menor peso inserido e: {lista[1]}')
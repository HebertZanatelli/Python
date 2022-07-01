lista = []
for c in range(1, 6):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print('=-'*30)
print(f'Você digitou os valores: {lista}')
num = sorted(lista)
print(f'\nO maior valor digitado foi {num[-1]} na posição(ões) ', end='')
for i, v in enumerate(lista):
    if v == num[-1]:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {num[0]} na posição(ões) ', end='')
for i, v in enumerate(lista):
    if v == num[0]:
        print(f'{i}...', end='')

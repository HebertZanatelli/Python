pessoa = []
dados = []
maior = menor = 0
while True:
    dados.append(input("Nome: "))
    dados.append(float(input('Peso: ')))
    if len(pessoa) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoa.append(dados[:])
    dados.clear()
    parar = input('Deseja continuar? [S/N]').upper().strip()
    while parar != 'S' and parar != 'N':
        parar = input('Deseja continuar? [S/N]').upper().strip()
    if parar == 'N':
        break
print(f'Ao todo, você cadastrou {len(pessoa)} Pessoas.')

print(f'O maior peso encontrado foi: {maior}Kg. Os pesos sao de :', end=' ')
for p in pessoa:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' e ')
print(f'\nO menor peso encontrado foi: {menor}Kg. Os pesos sao de :', end=' ')
for p in pessoa:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' e ')
        
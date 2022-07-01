pessoa = []
dados = []
todos_pesos = []
while True:
    dados.append(input("Nome: "))
    dados.append(float(input('Peso: ')))
    pessoa.append(dados[:])
    todos_pesos.append(dados[1:])
    dados.clear()
    parar = input('Deseja continuar? [S/N]').upper().strip()
    while parar != 'S' and parar != 'N':
        parar = input('Deseja continuar? [S/N]').upper().strip()
    if parar == 'N':
        break
maior = max(todos_pesos)
menor = min(todos_pesos)
print('-='*20)
print(f'Ao todo, foram cadastradas {len(pessoa)}')
print(f'O maior peso cadastrado foi: {maior[0]}KG. Peso de: ', end='')
for p in pessoa:
    if p[1] == maior[0]:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso cadastrado foi: {menor[0]}KG. Peso de: ', end='')
for p in pessoa:
    if p[1] == menor[0]:
        print(f'[{p[0]}]', end=' ')
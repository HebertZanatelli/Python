principal = []
dados = []
tot_idade = []
while True:
    dados.append(input('Nome:'))
    dados.append(int(input('Idade: ')))
    parar = input('Deseja continuar? [S/N]').upper().strip()
    principal.append(dados[:])
    tot_idade.append(dados[1:])
    dados.clear()
    while parar != 'N' and parar != 'S':
        parar = input('Deseja continuar? [S/N]').upper().strip()
    if parar == 'N':
        break
maior = max(tot_idade)
menor = min(tot_idade)
print(f'O numero de pessoas cadastrada é {len(principal)}')
print(f'A maior idade encontrada é: {maior[0]} anos. Idade de:', end='')
for p in principal:
    if p[1] == maior[0]:
        print(f'[{p[0]}]', end=' ')
print(f'\nA menor idade encontrada é: {menor[0]} anos. Idade de: ', end='')
for p in principal:
    if p[1] == menor[0]:
        print(f'[{p[0]}]', end=' ')

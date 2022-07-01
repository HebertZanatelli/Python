valor = []
while True:
    num = int(input('Digite um valor para adicionar na lista: '))
    if num not in valor:
        print('Valor adicionado com sucesso...')
        valor.append(num)
    else:
        print('Valor Duplicado! Não vou adicionar...')
    opcao = input('Deseja continuar? [S/N]').upper().strip()
    while opcao != 'S' and opcao != 'N':
        print('Opção incorreta, informe novamente:')
        opcao = input('Deseja continuar? [S/N]').upper().strip()
    if opcao == 'N':
        break
print('-=' * 30)
print(f'Você digitou os valores {sorted(valor)}')

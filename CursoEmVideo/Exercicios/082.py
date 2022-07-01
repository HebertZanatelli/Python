lista =[]
listaimpar = []
listapar = []
while True:
    num = int(input('Insira um numero para criar uma lista: '))
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    opcao = input('Deseja continuar? [S/N]').upper().strip()
    while opcao != 'N' and opcao != 'S':
        print('Você digitou a opção invalida.')
        opcao = input('[S/N]').upper().strip()
    if opcao == 'N':
        break
print(f'A lista COMPLETA é: {lista}')
print(f'A lista de PARES é: {listapar}')
print(f'A lista de ÍMPARES é: {listaimpar}')
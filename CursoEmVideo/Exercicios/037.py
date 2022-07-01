while True:
    numero = int(input('Digite um numero: '))

    print('Escolha uma das Bases para CONVERSÃO')
    print('[1] Converter para BINÁRIO;')
    print('[2] Converter para OCTAL;')
    print('[3] Converter para HEXADECIMAL')
    opcao = input('Digite sua opção:')

    if opcao == '1':
        binario = bin(numero)
        print(f'O {numero} em BINÁRIO é: {binario.upper()[2:]}')
    elif opcao == '2':
        octal = oct(numero)
        print(f'O {numero} em OCTAL é: {octal.upper()[2:]}')
    elif opcao == '3':
        hexa = hex(numero)
        print(f'O {numero} em HEXADECIMAL é: {hexa.upper()[2:]}')
    else:
        print('Opção inválida. tente novamente.')
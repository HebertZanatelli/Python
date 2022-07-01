opcao = 0
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
while opcao != 5:

    print('Opções:')
    print('     [1] SOMAR')
    print('     [2] MULTIPLICAR')
    print('     [3] MAIOR')
    print('     [4] NOVOS NÚMEROS')
    print('     [5] SAIR DO PROGRAMA')

    opcao = int(input('Escolha Uma opção: '))
    if opcao == 4:
        print('Informe os numeros novamente:')
        num1 = int(input('Digite o primeiro numero: '))
        num2 = int(input('Digite o segundo numero: '))
    elif opcao == 1:
        print(f'A soma entre {num1} + {num2} é {num1+num2}')
    elif opcao == 2:
        print(f'O resultado de {num1} x {num2} é {num1 * num2}')
    elif opcao == 3:
        if num1 > num2:
            print(f'Entre {num1} e {num2}, o maior valor é {num1}')
        elif num2 > num1:
            print(f'Entre {num1} e {num2}, o maior valor é {num2}')
        else:
            print(f'Os valores entre {num1} e {num2} são iguais')
    elif opcao == 5:
        print('Fim do programa, volte sempre')
    else:
        print('Opção Invalida, tente novamente.')



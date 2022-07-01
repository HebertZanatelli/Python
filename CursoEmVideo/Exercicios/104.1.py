def leiaInt(msg):
    while True:
        n = input(msg)

        if n.isnumeric():
            print(f'Você Digitou o Numero {n}.')
            break
        else:
            print('Erro! Digite um numero inteiro válido')


n = leiaInt('Digite um numero: ')
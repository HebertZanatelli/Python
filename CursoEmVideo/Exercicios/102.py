def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o detalhe do fatorial.
    :return: O valor do Fatorial do numero N escolhido.
    """
    f = 1
    cont = num
    print(f'{num}! ', end='')
    while cont >= 1:
        f *= cont
        if show:
            if cont != 1:
                print(f'{cont} x', end=' ')
            if cont == 1:
                print(cont, end=' ')
        cont -= 1
    return f'= {f}'


# Programa Principal
numero = int(input('Digite o numero para exbir sua fatorial: '))
while True:
    opcao = input('Deseja exibir a fatorial detalada? [S/N]').strip().upper()[0]
    if opcao in 'SN':
        break
    else:
        print('Opção incorreta, digite apenas "S" ou "N"')
if opcao == 'S':
    opcao = True
else:
    opcao = False
print(fatorial(numero, opcao))

help(fatorial)

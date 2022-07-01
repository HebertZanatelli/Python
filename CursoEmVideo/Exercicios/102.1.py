def fatorial(num, opcao=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o detalhe do fatorial.
    :return: O valor do Fatorial do numero N escolhido.
    """
    f = 1
    for c in range(num, 0, -1):
        if opcao:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} = ', end='')
        f *= c
    return f


detalhe = input('Digite S/N para exibir opção detalhada: ').strip().upper()
if detalhe == 'S':
    detalhe = True
else:
    detalhe = False
fat = int(input('Digite um numero para criar sua fatorial: '))
# print(fatorial(fat, detalhe))
help(fatorial)

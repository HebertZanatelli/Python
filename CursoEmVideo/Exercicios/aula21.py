# def contador(i, f, p):
#     """
#     -> faz uma contagem e mostra na tela.
#     :param i: inicio da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     Função criada por Hebert Alves
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end='..')
#         c += p
#     print('FIM!')
#
#
# contador(2, 10, 2)
# help(contador)
#
# help(print)
#
#
# def somar(a, b, c=0):  # se nao passar o parametro e C, ele adota o 0 pois foi pré definido
#     s = a + b + c
#     print(f'A soma vale {s}')
# somar(8, 4)


# def funcao():
#     n1 = 4
#     print(f'N1 dentro vale {n1}')
#
# n1 = 2
# funcao()
# print(f'N1 fora vale {n1}')


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')

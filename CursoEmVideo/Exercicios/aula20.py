# def lin():
#     print('-' * 30)
#
#
# lin()
# print('     CURSO EM VÍDEO     ')
# lin()
# lin()
# print('     APRENDA PYTHON      ')
# lin()
# lin()
# print('     HEBERT AUGUSTO      ')
# lin()
#
#
# def soma(a, b):
#     s = a + b
#     print(s)
#     print('-' * 30)
#
#
# soma(5, 2)
# soma(6, 4)
#
#
# def msg(msg):
#     print('-' * 30)
#     print(msg)
#     print('-' * 30)
#
#
# msg("Sistema de Alunos")
# msg("Cadastro de Funcionários")
# msg("Erro do Sistema.")

# def contador(*num):  # *num informa que vai desempacotar varios atributos como parametros.
#     tam = len(num)
#     print(f'Recebi os valores de {num} e ao todo são {tam} numeros')
#
# #PROGRAMA PRINCIPAL
# contador(2,3,1,4,5)
# contador(8,0)
# contador(4,4,7,6,2)

# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1
# valores = [4, 2, 6, 1, 0, 7, 3]
# dobra(valores)
# print(valores)

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores}, temos o total de {s}')


soma(5, 2)
soma(3, 1, 10)
soma(5, 9, 3)

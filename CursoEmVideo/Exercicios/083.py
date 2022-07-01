expressao = input('Digite a expressão: ')
a = expressao.count('(')
b = expressao.count(')')

if b == a:
    print('Está expressão é válida!')
else:
    print('Está expressão NÃO é válida!')

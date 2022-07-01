def saudacao(msg='olá', nome='teste'):
    print(msg, nome)


saudacao(nome='zezinho', msg='salvee')
saudacao('teste', '123')
saudacao('zeca', 'urubu')
saudacao('olá', 'mundo')


def funcao(var):
    return var


variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')

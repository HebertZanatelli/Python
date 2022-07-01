import random
a = input('Digite o 1º aluno: ')
b = input('Digite o 2º aluno: ')
c = input('Digite o 3º aluno: ')
d = input('Digite o 4º aluno: ')

lista = [a,b,c,d]


escolhido = random.choice(lista)

print(f'O aluno escolhido foi: {escolhido}')
import random
num = int(input("Digite um numero entre 0 e 5: "))
teste = random.randint(0,6)

if num == teste:
    print('Parabens, Você acertou!')
else:
    print(f' {teste}:( voce errou')
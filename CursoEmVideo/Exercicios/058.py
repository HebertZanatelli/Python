import random
computador = random.randint(0, 10)
palpite = ''
tentativas = 0
print('Sou seu computador...')
print('Acabei de pensar em um numero entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
while computador != palpite:
    palpite = int(input('Qual o seu palpite? '))
    if palpite > computador:
        print('Menos, tente mais uma vez...')
    else:
        print('Mais, tente mais uma vez...')
    tentativas += 1

print(f'Você acertou com {tentativas} Tentativas, PARABÉNS!')

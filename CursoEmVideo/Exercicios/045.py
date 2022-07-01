import time
import random
while True:
    print('Suas Opçoes: ')
    print('[0] PEDRA')
    print('[1] PAPEL')
    print('[2] TESOURA')
    jogada = int(input('Selicione a sua jogada: '))
    print('JO')
    time.sleep(0.2)
    print("KEN")
    time.sleep(0.2)
    print('PO!!')
    computador = random.randint(0,2)

    if jogada == 0 and computador == 0:
        print('=-' * 15)
        print('O Computador jogou Pedra')
        print('O jogador jogou Pedra')
        print('=-' * 15)
        print('EMPATE!!')
    elif jogada == 0 and computador == 1:
        print('=-' * 15)
        print('O Computador jogou Papel')
        print('O jogador jogou Pedra')
        print('=-' * 15)
        print('O Computador VENCEU!!')
    elif jogada == 0 and computador == 2:
        print('=-' * 15)
        print('O Computador jogou Pedra')
        print('O jogador jogou Pedra')
        print('=-' * 15)
        print('O Jogador VENCEU!!!')

    elif jogada == 1 and computador == 0:
        print('=-' * 15)
        print('O Computador jogou Pedra')
        print('O jogador jogou Papel')
        print('=-' * 15)
        print('O Jogador VENCEU!!!')
    elif jogada == 1 and computador == 1:
        print('=-' * 15)
        print('O Computador jogou Papel')
        print('O jogador jogou Papel')
        print('=-' * 15)
        print('EMPATE!!')
    elif jogada == 1 and computador == 2:
        print('=-' * 15)
        print('O Computador jogou Tesoura')
        print('O jogador jogou Papel')
        print('=-' * 15)
        print('O Computador VENCEU!!')
    elif jogada == 2 and computador == 0:
        print('=-' * 15)
        print('O Computador jogou Pedra')
        print('O jogador jogou Tesoura')
        print('=-' * 15)
        print('O Computador VENCEU!!')
    elif jogada == 2 and computador == 1:
        print('=-' * 15)
        print('O Computador jogou Papel')
        print('O jogador jogou Tesoura')
        print('=-' * 15)
        print('O Jogador VENCEU!!')
    elif jogada == 2 and computador == 2:
        print('=-' * 15)
        print('O Computador jogou Tesoura')
        print('O jogador jogou Tesoura')
        print('=-' * 15)
        print('EMPATE!!')

    print('')





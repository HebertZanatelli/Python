import random
import time

placarComp = 0
placarJog = 0
while True:

    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = random.randint(0, 2)
    print('''Suas Opções:
    [0]PEDRA
    [1]PAPEL
    [2]TESOURA''')
    jogador = int(input("Digite a sua jogada:"))
    print("JO")
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!')
    print('-=' * 12)
    print(f'Computador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}')
    print('-=' * 12)
    if computador == 0:
        if jogador == 0:
            print('EMPATE!!')
        elif jogador == 1:
            print('Jogador VENCE!!!')
            placarJog = placarJog + 1

        elif jogador == 2:
            print('Computador VENCE!!')
            placarComp = placarComp + 1

        else:
            print('Opção IVALIDA')

    elif computador == 1:
        if jogador == 0:
            print('Computador VENCE!!')
            placarComp = placarComp + 1
        elif jogador == 1:
            print('EMPATE!!')
        elif jogador == 2:
            print('Jogador VENCE!!')
            placarJog = placarJog + 1
        else:
            print('Opção IVALIDA')

    elif computador == 2:
        if jogador == 0:
            print('Jogador VENCE!!')
            placarJog = placarJog + 1

        elif jogador == 1:
            print('Computador VENCE!!')
            placarComp = placarComp + 1

        elif jogador == 2:
            print('EMPATE!!')

    else:
        print('Opção IVALIDA')
    print('')
    print('-='*12)
    print(f'PLACAR:')
    print(f'Jogador: {placarJog}')
    print(f'Computador {placarComp}')
    print('-='*12)


import random
pj = 0
while True:
    print('=-'*15)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-'*15)
    num = int(input('Digite um numero: '))
    pij = ' '
    while pij not in 'PI':
        pij = input('Par ou Ímpar? [P/I]').strip().upper()[0]
    numPC = random.randint(0, 10)
    total = num + numPC
    if total % 2 == 0:
        print(f'Você jogou {num} e o Computador jogou {numPC}, Total {total} = PAR')
        if pij == 'P' and total%2 == 0:
            print('Você VENCEU!!')
            pj += 1
        else:
            break
    else:
        print(f'Você jogou {num} e o Computador jogou {numPC}, Total {total} = ÍMPAR')
        if pij == 'I' and total % 2 != 0:
            print('Você VENCEU!!')
            pj += 1
        else:
            break
print('Você PERDEU!!')
print('=-'*15)
print(f'GAME OVER! Você venceu {pj} vez(es).')

import random
import time
cont = 1
jogador = {'jogador1': random.randint(1, 6),
           'jogador2': random.randint(1, 6),
           'jogador3': random.randint(1, 6),
           'jogador4': random.randint(1, 6), }
print('=== RESULTADOS ===')
for d, i in jogador.items():
    print(f'o {d} tirou {i} no dado')
    time.sleep(1)
print(' ===- RANKING -===')
for i in sorted(jogador, key=jogador.get, reverse=True):
    print(f'{cont}º Lugar: {i} - {jogador[i]} PTS  ')
    cont += 1
    time.sleep(1)









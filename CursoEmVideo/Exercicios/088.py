import random
import time
dados = []
jogos = []
print('=-' * 15)
print('         JOGA NA SENA     ')
print('=-' * 15)

qtd_jogos = int(input('Digite a quantidade de sorteios: '))
tot_jogos = 1

while tot_jogos <= qtd_jogos:
    while True:
        num = random.randint(1, 60)
        if num not in jogos and len(jogos) <= 6:
            jogos.append(num)
        if len(jogos) == 6:
            break
    dados.append(jogos[:])
    jogos.clear()
    tot_jogos += 1
print('-=' * 5, f'SORTEANDO {qtd_jogos} JOGOS', '-=' * 5)
for v, l in enumerate(dados):
    print(f'Jogo {v+1}: {sorted(l)}')
    time.sleep(1)
print('=-' * 5, 'BOA SORTE', '-=' * 5)

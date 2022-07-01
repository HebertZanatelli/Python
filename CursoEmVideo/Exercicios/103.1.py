def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')


jogador = input('Nome do Jogador: ')
gols = input('Número de Gols: ')

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if jogador.strip() == '':
    ficha(gol=gols)
else:
    ficha(jogador, gols)

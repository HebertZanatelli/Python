resultado = dict()
gols = []
resultado['nome'] = input('Nome do jogador: ')
partida = int(input(f'Quantas partidas {resultado["nome"]} jogou? '))
for c in range(partida):
    gol = int(input(f"  Quantos Gol fez na partida {c+1}? "))
    gols.append(gol)
resultado['gols'] = gols
resultado['total'] = sum(gols)
print('-=' * 30)
print(resultado)
print('-=' * 30)
for k, v in resultado.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {resultado["nome"]} jogou {partida} partidas.')
for c, g in enumerate(gols):
    print(f'    => Na partida {c+1}, fez {g} gols.')
print(f'Foi um total de {resultado["total"]} gols')
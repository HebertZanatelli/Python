resultado = dict()
gols = []
final = []
while True:
    resultado.clear()
    gols.clear()
    resultado['nome'] = input('Nome do jogador: ').title()
    partida = int(input(f'Quantas partidas {resultado["nome"]} jogou? '))
    for c in range(partida):
        gols.append(int(input(f"  Quantos Gol fez na partida {c+1}? ")))
    resultado['gols'] = gols[:]
    resultado['total'] = sum(gols)
    while True:
        parar = input('Deseja continuar? [S/N]').strip().upper()[0]
        if parar in 'SN':
            break
        print('ERRO! Digite "S" ou "N" apenas.')
    final.append(resultado.copy())
    if parar == 'N':
        break
print('-=' * 30)
print('Cod ', end='')
for i in resultado.keys():
    print(f'{i.title():<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(final):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(final):
        print(f'ERRO!Não existe jogador com código {busca}')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {final[busca]["nome"]}')
        for c, k in enumerate(final[busca]['gols']):
            print(f'   No jogo {c+1} fez {k} gols')
    print('-' * 40)
print('<< Volte Sempre >>')

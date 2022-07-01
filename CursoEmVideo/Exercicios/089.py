dados = []
while True:
    nome = input('Nome: ')
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    parar = input('Deseja continuar [S/N]').upper().strip()
    while parar != 'N' and parar != 'S':
        print('Opção Inválida. Tente novamente.')
        parar = input('Deseja continuar [S/N]').upper().strip()
    media = (nota_1 + nota_2) / 2
    dados.append([nome, [nota_1, nota_2], media])
    if parar == 'N':
        break
print('-=' * 30)
print(dados)
print(f'{"No.":<5}{"NOME":<10}{"MÉDIA":>8}')
print('-'*30)
for i, v in enumerate(dados):
    print(f'{i:<5}{v[0]:<10}{v[2]:>8.1f}')
while True:
    print('-=' * 25)
    aluno = int(input('Deseja mostrar notas de qual aluno? [999 para encerrar]'))
    if aluno == 999:
        print("Finalizando... ")
        break
    if aluno <= len(dados)-1:
        print(f'Aluno: {dados[aluno][0]}, notas: {dados[aluno][1]}')


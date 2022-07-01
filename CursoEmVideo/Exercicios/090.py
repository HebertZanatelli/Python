boletim = {'nome': input('Nome do aluno: '), 'media': float(input('Média do aluno: '))}
print('=-'*30)

if boletim['media'] >= 7.0:
    boletim['situacão'] = 'Aprovado'
elif boletim['media'] >= 5 and boletim['media'] < 7.0:
    boletim['situacão'] = 'Recuperação'
else:
    boletim['situacão'] = 'Reprovado'
for v, k in boletim.items():
    print(f'- {v} é igual a {k}')
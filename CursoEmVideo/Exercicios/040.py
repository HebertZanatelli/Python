nota1 = float(input('Insira a Primeira nota: '))
nota2 = float(input('Insira a Segunda Nota: '))

media = (nota1 + nota2) / 2

print(f'Tirando {nota1} e {nota2}, a média do aluno é: {media}.')
if media < 5.0:
    print(f'O aluno está REPROVADO')
elif media >= 7.0:
    print(f'O aluno está APROVADO')
else:
    print('O aluno está de RECUPERAÇÃO')

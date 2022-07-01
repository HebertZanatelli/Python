nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
nota3 = float(input('Digite a terceira nota do aluno: '))

div = [nota1,nota2, nota3]

media = (nota1 + nota2 + nota3) / len(div)

print(f'A média da nota do aluno é: {media:.1f}')
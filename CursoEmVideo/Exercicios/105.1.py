# def notas(*n, sit=False):
#     dic = {'total': len(n), 'maior': max(n), 'menor': min(n),
#            'media': (sum(n)/len(n))}
#     if sit:
#         if dic['media'] >= 7:
#             dic['situacao'] = 'Aprovado'
#         elif 7 > dic['media'] >= 5:
#             dic['situacao'] = 'Recuperação'
#         else:
#             dic['situacao'] = 'Reprovado'
#
#     return dic
#
# #Programa Principal
# lista = []
# while True:
#     nota = float(input('Digite uma nota para adicionar: '))
#     lista.append(nota)
#
#     while True:
#         opcao = input('Deseja continuar adicionando nota: [S/N]').upper().strip()
#         if opcao in 'SN':
#             break
#         else:
#             print('Opção Inválida, tente Novamente.')
#     if opcao == 'N':
#         break
# while True:
#     situacao = input('Deseja informar a Situação do aluno? [S/N]').upper().strip()
#     if situacao in 'SN':
#         if situacao == 'S':
#             situacao = True
#             break
#         else:
#             situacao = False
#             break
#     else:
#         print('Opção Incorreta! Digite S ou N para definir a situação do Aluno ')
#
#
# print(notas(lista, sit=situacao))

def notas(*nota,sit=True    ):
    """
    -> Função para analisar notas e situações de vários alunos
    :param nota: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    maior = menor = media = soma_notas = 0
    situacao = ''
    dicionario_alunos = dict()
    for contador, notas_alunos in enumerate(nota):
        if contador == 0:
            maior = notas_alunos
            menor = notas_alunos
        else:
            if notas_alunos > maior:
                maior = notas_alunos
            if notas_alunos < menor:
                menor = notas_alunos
        soma_notas += notas_alunos
    media = soma_notas / len(nota)
    dicionario_alunos['Total'] = len(nota)
    dicionario_alunos['maior'] = maior
    dicionario_alunos['menor'] = menor
    dicionario_alunos['média'] = media
    if sit:
        if media >= 7:
            situacao = 'Boa'.upper()
        elif 6 <= media < 7:
            situacao = 'Razoável'.upper()
        else:
            situacao = 'RUIM'
        dicionario_alunos['situação'] = situacao
    return dicionario_alunos


#Programa principal

resp = notas(3.5, 2, 6.5, 2, 7, 4)
print(resp)
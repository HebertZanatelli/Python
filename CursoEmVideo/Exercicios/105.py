def notas(*nota, sit=False):
    """
    ->Função para analisar a situação e notas dos alunos:
    :param num: uma ou mais notas dos alunos(aceita várias)
    :param sit: valor opicional no qual mostra a situação do aluno (boa, razoavel ou ruim)
    :return: retorna um dicionario com a maior, menor, média e quantas notas foram informadas.
    """
    r = {'total': len(nota), 'maior': max(nota), 'menor': min(nota), 'média': sum(nota) / len(nota)}
    if sit:
        if r['média'] >= 7:
            r['Situação'] = 'Boa'
        elif r['média'] >= 5:
            r['Situação'] = 'Razoável'
        else:
            r['Situação'] = 'Ruim'
    return r


resp = notas(5.5, 8.5, 9.5, sit=True)
print(f'{resp}')

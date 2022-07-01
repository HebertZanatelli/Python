def voto(ano):
    import datetime
    atual = datetime.date.today().year
    idade = atual - ano
    if idade < 16:
        return f'No Brasil, com {idade} anos, o voto é NEGADO.'
    elif 16 <= idade < 18 or idade > 65:
        return f'No Brasil, com {idade} anos, o voto é OPICIONAL.'
    else:
        return f'No Brasil, com {idade} anos, o voto é OBRIGATÓRIO.'


print(voto(int(input('Digite o Ano de Nascimento: '))))

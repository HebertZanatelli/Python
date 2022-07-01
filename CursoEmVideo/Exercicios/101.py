def voto(ano):
    import datetime
    atual = datetime.date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos, o voto não é obrigatório.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos, o voto é opcional.'
    else:
        return f'Com {idade} anos, o voto é obrigatório.'


# Programa Principal
print(voto(int(input('Digite o ano de Nascimento: '))))

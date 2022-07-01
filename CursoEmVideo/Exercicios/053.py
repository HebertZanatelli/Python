 #solução mais simples, aprendida nos comentários do curso.
frase = input('Digite uma frase: ')
teste = frase.replace(' ','')
final = teste[::-1]
if teste == final:
    print("é um polidromo")
else:
    print('não é um polidromo')

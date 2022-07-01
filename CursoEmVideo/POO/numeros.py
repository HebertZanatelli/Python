# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais
#
# Email Impacta: hebert.alves@aluno.faculdadeimpacta.com.br - EAD - ADS 2A


def eh_primo(n):
	"""Função que verifica se um número é primo

	Recebe um número natural n, com n >= 2, e retorna verdadeiro se
	n é um número primo e falso caso contrário.

	Exemplos
	--------
	Um número é dito primo se possuir apenas 2 divisores, isto é,
	não possuir nenhum divisor além do 1 e do próprio n.
	29 é primo:
		divisores de 29: 1, 29
	30 NÃO é primo:
		divisores de 30: 1, 2, 3, 5, 6, 10, 15, 30

	Parâmetros
	----------
	n : int
		Número natural a ser testado.

	Retorno
	-------
	bool
		True se n for um número primo e False caso contrário.
	"""
	qtd_divisores = 0
	candidato = 1
	while candidato <= n:
		if n % candidato == 0:
			qtd_divisores += 1
		candidato += 1
	if qtd_divisores == 2:
		return True
	else:
		return False


def lista_primos(n):
	"""Função que retorna uma lista de primos até n

	Recebe um número natural n, com n >= 2, e retorna uma
	lista com todos o números primos estritamente menores
	que n, em ordem crescente.

	Parâmetros
	----------
	n : int
		Número natural que define o limite superior da lista.

	Retorno
	-------
	list
		itens : int
		descrição : Lista com todos os números primos menores
			que n, em ordem crescente.
	"""
	lista = []
	for i in range(2, n):  # i varia de 2 até n-1
		if eh_primo(i):  # testa se i é um número primo
			lista.append(i)  # adiciona i ao final da lista, se i for um número primo
	return lista


def conta_primos(s):
	"""Função que conta a quantidade de primos em uma sequência

	Recebe uma sequência de números naturais s e retorna
	um dicionário com a contagem de ocorrências de cada número
	primo da sequência. Números não primos devem ser ignorados.
	Os números da sequência serão sempre maiores ou iguais a 2.

	Exemplos
	--------
	Caso s = [11, 2, 3, 4, 11, 2, 5, 2]
		O retorno deverá ser: {11: 2, 2: 3, 3: 1, 5: 1}
	Caso s = [1, 4, 8, 10]
		O retorno deverá ser: {}
	Caso s = (111, 191, 202, 306, 239, 579)
		O retorno deverá ser: {191: 1, 239: 1}

	Parâmetros
	----------
	s : list | tuple
		itens : int
		descrição : Uma sequência arbitrária de números naturais.

	Retorno
	-------
	dict
		chave : int
		valor : int
		descrição : a chave é o número primo e o valor
			o total de ocorrências do número primo na
			sequência s.
	"""

	d = {}
	for num in s:
		if eh_primo(num) and num >= 2:
			if num in d:
				valor  = d[num]
				d[num] = valor + 1
			else:
				d[num] = 1
	return d


def eh_armstrong(n):
	"""Função que verifica se um número é de Armstrong

	Recebe um número natural n, com n >= 0, e retorna
	verdadeiro se n é um número de Armstrong e falso
	caso contrário.

	Exemplos
	--------
	Um número é dito número de Armstrong se a soma de seus digitos
	elevados ao número total de digitos é igual a ele próprio.
	153 é número de Armstrong:
		1**3 + 5**3 + 3**3 = 1 + 125 + 27 = 153
	4 é número de Armstrong:
		4 ** 1 = 4

	Parâmetros
	----------
	n : int
		Número natural a ser testado.

	Retorno
	-------
	bool
		True se n for um número de Armstrong e False caso contrário.
	"""
	s = 0                                                     
	k = n                                                     
	while k>0:                                                
		d = k%10                                              
		s = s + (d**len(str(n)))                                        
		k = k//10                                             
	if n == s:                                                
		return (True)
	else:                                                       
		return (False)

def eh_quase_armstrong(n):
	"""Função que verifica se um número é quase de Armstrong

	Recebe um número natural n, com n >= 0, e retorna
	verdadeiro se n atende aos seguintes critérios:

	1) não ser um número de Armstrong;
	2) o resultado da soma de seus digitos elevados ao número total
	   de digitos é igual a ele próprio somado ou subtraído de 1.

	Exemplos
	--------
	35 é quase um número de Armstrong:
		3**2 + 5**2 = 9 + 25 = 34
	75 é quase um número de Armstrong:
		7**2 + 5**2 = 49 + 25 = 74

	Parâmetros
	----------
	n : int
		Número natural a ser testado.

	Retorno
	-------
	bool
		True se n for um número quase de Armstrong e False caso contrário.
	"""
	s = 0                                                     
	k = n                                                     
	while k>0:                                                
		d = k%10                                              
		s = s + (d**len(str(n)))                                        
		k = k//10                                             
	if n-1 == s or n+1==s:                                                
		return (True)
	else:                                                       
		return (False)


def lista_armstrong(n):
	"""Função que lista os números e Armstrong até n

	Recebe um número natural n e retorna uma lista com todos o
	números de Armstrong estritamente menores que n, em ordem crescente.

	Parâmetros
	----------
	n : int
		Número natural que define o limite superior da lista.

	Retorno
	-------
	list
		itens : int
		descrição : Uma lista contendo todos os números de Armstrong
			menores que n, em ordem crescente.
	"""
	lista = []
	for i in range(0,n):
		if eh_armstrong(i):
			lista.append(i)

	return(lista)


def eh_perfeito(n):
	"""Função que verifica se um número é dito perfeito

	Recebe um número natural n, com n >= 2, e retorna verdadeiro se
	n é dito um número perfeito e falso caso contrário

	Exemplos
	--------
	Um número é dito perfeito se a soma de todos os divisores próprios é
	igual a ele mesmo.
	6 é um número perfeito:
		divisores próprios de 6: 1, 2, 3
		1 + 2 + 3 = 6
	12 NÃO é um número perfeito:
		divisores próprios de 12: 1, 2, 3, 4, 6
		1 + 2 + 3 + 4 + 6 = 16

	Parâmetros
	----------
	n : int
		Número natural a ser testado.

	Retorno
	-------
	bool
		True se n for um número perfeito e False caso contrário.
	"""
	soma=0
	for val in range(1,n):
		if n % val == 0:
			soma += val

	if soma==n:
		return True
	else:
		return False


def lista_perfeitos(n):
	"""Função que lista os números ditos perfeitos até n

	Recebe um número natural n, com n >= 2, e retorna uma lista
	com todos os números perfeitos estritamente menores que n,
	em ordem crescente.

	Parâmetros
	----------
	n : int
		Número natural que define o limite superior da lista.

	Retorno
	-------
	list
		itens : int
		descrição : Uma lista contendo todos os números perfeitos
			menores que n em ordem crescente.
	"""
	lista = []
	for i in range(2,n):
		if eh_perfeito(i):
			lista.append(i)

	return(lista)

'''Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar.'''

numero = int(input('Digite um número para saber se é par ou impar: '))
resto = numero % 2

if resto == 0:
    print('Número é par')
else:
    print('Número é impar')
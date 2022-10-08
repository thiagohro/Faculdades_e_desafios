''' - Lista de Exercício Estácio 
- Paradigmas de Linguagens de Programação em Python 
- Aluno : Thiago Henrique Rezende de Oliveira
- Matrícula: 201201387061 
- Exercício 01 
- Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
a. Para homens: (72.7*h) - 58
b. Para mulheres: (62.1*h) - 44.7 '''

homem_ou_mulher = 0

while homem_ou_mulher != 1 and homem_ou_mulher != 2:    
    homem_ou_mulher = int(input('Selecione: 1- Sexo Masculino ou 2- Sexo Feminino: '))    

h = float(input('Qual altura: '))
peso = float(input('Qual peso: '))

if homem_ou_mulher == 1:
	peso_ideal = (72.7*h) - 58
else:
	peso_ideal = (62.1*h) - 44.7

if peso < peso_ideal:
	print('Abaixo do peso ideal!')
elif peso == peso_ideal:
	print('Dentro do peso ideal!')
else:
	print('Acima do peso ideal!')
print ('Peso: %.2f / Peso ideal: %.2f' %(peso, peso_ideal))
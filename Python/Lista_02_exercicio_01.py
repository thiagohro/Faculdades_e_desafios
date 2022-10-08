'''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''


valor_saque = int(input("Informe o valor que deseja sacar (valor maior que R$10 e menor que 600): "))
while(valor_saque < 10 or valor_saque > 600):
    print('Valor inválido! Digite um valor maior que R$10 e menor que R$600.')
    valor_saque = int(input('Digite o valor para saque: '))

notas_de_100 = int((valor_saque - (valor_saque%100))/100)
notas_de_50 = int((valor_saque%100)/50)
notas_de_10 = int(((valor_saque%50)/10))
notas_de_5 = int(((valor_saque%10)/5))
notas_de_1 = int(((valor_saque%5)/1))

if(notas_de_100 == 1):
    print(f'{notas_de_100} nota de R$100')
elif(notas_de_100 > 1):
    print(f'{notas_de_100} notas de R$100')
if(notas_de_50 == 1):
    print(f'{notas_de_50} nota de R$50')
elif(notas_de_50 > 1):
    print(f'{notas_de_50} notas de R$50')
if(notas_de_10 == 1):
    print(f'{notas_de_10} nota de R$10')
elif(notas_de_10 > 1):
    print(f'{notas_de_10} notas de R$10')
if(notas_de_5 == 1):
    print(f'{notas_de_5} nota de R$5')
elif(notas_de_5 > 1):
    print(f'{notas_de_5} notas de R$5')
if (notas_de_1 == 1):
    print(f'{notas_de_1} nota de R$1')
elif (notas_de_1 > 1):
    print(f'{notas_de_1} notas de R$1')
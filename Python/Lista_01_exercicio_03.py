'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido, conforme a tabela abaixo: 
    + Salário Bruto : R$ 
    - IR (11%) : R$ 
    - INSS (8%) : R$ 
    - Sindicato ( 5%) : R$ 
    = Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.'''

sal_hora = float(input("Quanto você ganha por hora? "))
horas_trab_mes = int(input("Quantas horas você trabalha no mês? "))
salario = sal_hora * horas_trab_mes

ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
sal_liquido = salario - ir - inss - sindicato

print("Salário bruto: %.2f" %salario, "\nIR: %.2f" %ir, "\nINSS: %.2f" %inss, "\nSindicato %.2f" %sindicato, "\nSalário Liquido: %.2f" %sal_liquido)
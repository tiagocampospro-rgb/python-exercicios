#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
salario = float(input('Qual seu salário atual?'))
aumento = salario * 0.15
salarioatualizado = salario + aumento
print('Seu novo salário é de: {:.2f}'.format(salarioatualizado))

#DESAFIO #030 - Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
numero = int(input('Digite um númeiro:'))
resultado = numero % 2
#Regra matemática: o RESTO DA DIVISÃO de qualquer número PAR, por 2 será igual a 0
#Regra matemática: O RESTO DA DIVISÃO de qualquer número IMPAR, por 2 será igual a 1
if resultado == 0:
    print('O número \033[32m{} é PAR\033[m'.format(numero))
else:
    print('O número \033[31m{} é ÍMPAR\033[m'.format(numero))
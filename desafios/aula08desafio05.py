#DESAFIO 020 (5 da aula 8) - O mesmo professor do desafio anterior a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro grupos e o sorteie
import random
g1 = str(input('Nome do grupo 1:'))
g2 = str(input('Nome do grupo 2:'))
g3 = str(input('Nome do grupo 3:'))
g4 = str(input('Nome do grupo 4:'))
lista = [g1, g2, g3, g4]
random.shuffle(lista)
print('A ordem do grupo é {}')
print(lista)
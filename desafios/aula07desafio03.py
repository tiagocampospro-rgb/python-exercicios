# Desenvolva um programa que leia as duas notas de um aluno e calcule sua média
n1 = float(input('Digite sua nota:'))
n2 = float(input('Digite sua nota:'))
media = (n1 + n2) / 2
print('Sua média foi: \033[0;32m{}\033m'.format(media))
#DESAFIO 026 - Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A"
# - Em que posição ela aparece a primeira vez
# - Em que posição ela aparece a última vez
frase = str(input('Digite uma frase: ')).upper().strip()
print('Em sua frase aparece {} vezes a letra A'.format(frase.count('A')))
print('A letra A aparece primeiro na posição {}' .format(frase.find('A')+1))
print('A letra A aparece pela última vez na posição {}'.format(frase.rfind('A')+1))
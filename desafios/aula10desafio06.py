#DESAFIO 033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
# CRIEI SOZINHO A LÓGICA DA SOLUÇÃO
a = int(input('Primeito valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
if a > b and a > c:
    print('O número maior é o {}'.format(a))
if b > c and b > a:
    print('O número maior é o {}'.format(b))
if c > a and c > b:
    print('O número maior é o {}'.format(c))
if a < b and a < c:
    print('O número menor é o {}'.format(a))
if b < c and b < a:
    print('O número menor é o {}'.format(b))
if c < a and c < b:
    print('O número menor é o {}'.format(c))
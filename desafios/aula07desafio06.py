#DESAFIO: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela consegue comprar
#Cotação atual: 5.43
reais = float(input('Quantos reais você tem?'))
dolares = reais / 5.43

print('Você pode comprar {:.2f} dólares'.format(dolares))
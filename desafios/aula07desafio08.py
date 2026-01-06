#DESAFIO: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço:'))
desconto = preco * 0.05
precocomdesconto = preco - desconto

print('Seu valor com desconto é de {:.2f}'.format(precocomdesconto))
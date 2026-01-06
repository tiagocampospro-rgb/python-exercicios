# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n1 = int(input('Digite um valor em metros:'))
centimetros = n1 * 100
milimetros = n1 * 1000
print('Seu valor em centímetros é: {} e seu valor em milímetros é: {}'.format(centimetros, milimetros))

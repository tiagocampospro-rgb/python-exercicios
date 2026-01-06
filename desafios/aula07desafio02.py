# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n1 = float(input('Digite um número:'))
dobro = float(n1) * 2
triplo = float(n1) * 3
raiz = n1 ** (1/2)
print('Seu resultado: {}, {}, {:.2f}' .format(dobro, triplo, raiz))
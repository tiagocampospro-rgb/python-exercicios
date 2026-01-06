#DESAFIO: Faça um programa que leia a altura e a largura de uma parede em metros, calcule a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
alt = float(input('Digite a altura da sua parede: '))
larg = float(input('Digite a largura da sua parede: '))
area = alt * larg
litrodetinta = area / 2

print('Você precisa de {:.2f} litros de tinta.'.format(litrodetinta))
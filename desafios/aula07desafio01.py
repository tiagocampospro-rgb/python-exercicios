#Crie um programa que leia dois números e crie a soma entre eles, seu sucessor e seu antecessor.
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
s = n1 + n2
antecessor = s -1
sucessor = s +1
print('Seu resultado:', s)
print('Sucessor:{}'.format(sucessor))
print('antecessor{}'.format(antecessor))
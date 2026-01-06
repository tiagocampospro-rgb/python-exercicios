n1 = float(input('Digite sua nota:'))
n2 = float(input('Digite sua nota:'))
media = (n1 + n2) / 2
print('Seu média é de {}'.format(media))
if media <=6:
    print('Você precisa melhorar')
else:
    print('Parabéns, você está indo muito bem!')
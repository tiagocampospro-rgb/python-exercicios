from random import randint
from time import sleep #Para parecer que o computador está pensando
computador = randint(0,5) #faz o computador pensar
print('-=-' * 20) #Enfeite
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20) #Enfeite
jogador = int(input('Em que número eu pensei?')) #O jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns, você acertou!')
else:
    print('Você errrrrrrrrou! hahahaha')
print('O número que eu pensei foi {}'.format(computador))
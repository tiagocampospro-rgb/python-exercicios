#DESAFIO 029 - Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 para cada km acima do limite.
velocidade = float(input('Qual a velocidade atual do carro?')) #Usar Float para velocidade.
if velocidade > 80:
    print('\033[31mMULTADO! Você foi multado por estar acima da velocidade permitida: 80km/h\033[m')
    multa = (velocidade - 80) * 7
else:
    print('\033[32mVocê está dirigindo dentro do permitido.\033[m')
if velocidade > 80:
    print('\033[31mSua multa é de R${:.2f}!\033[m'.format(multa))
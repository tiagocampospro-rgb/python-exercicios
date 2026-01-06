distancia = float(input('Digite quantos km é sua viagem:'))
preco = distancia * 0.50
preco2 = distancia * 0.45
if distancia <= 200:
    print('O valor da sua viagem será \033[0;32mR${:.2f}\033[m'.format(preco))
else:
    print('O valor da sua viagem será R${:.2f}'.format(preco2))
    
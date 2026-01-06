print('-='*20)
print('Analisando triangulo')
print('-='*20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mOs segmentos acima \033[4mPODEM FORMAR\033[m um triangulo')
else:
    print('\033[31mOs segmentos acima \033[4mNÃO PODEM FORMAR\033[m um triangulo')
    
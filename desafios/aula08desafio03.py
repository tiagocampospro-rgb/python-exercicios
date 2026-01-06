import math
angulo = float(input('Digite um angulo:'))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('Valor de seno: {:.2f}'.format(seno))
print('Valor de coseno:{:.2f}'.format(coseno))
print('Valor do tangente:{:.2f}'.format(tan))

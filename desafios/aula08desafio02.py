from math import sqrt

co = float(input('Qual é o cateto oposto? '))
ca = float(input('Qual é o cateto adjacente? '))

x = co ** 2 + ca ** 2
hip = sqrt(x)

print(
    'Sabendo que o cateto oposto é {} e o cateto adjacente é {} '
    'o valor da hipotenusa é {:.2f}'.format(co, ca, hip)
)

# Crie um programa que leia o nome de unma cidade e diga se começa ou não como nome 'SANTO'
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
#praticando cores.
#Códigos para STYLE:
    # 0 = none | 1 = bold (negrito) | 4 = underline (sublinhar) | 7 = negative (inverter)
#Códigos para TEXT:
    # 97 = branco | 30 = pretp | 31 = vermelho | 32 = verde | 33 = amarelo | 34 = azul | 35 = roxo | 36 = azul claro | 37 = cinza
#Códigos para BACK:
    # 40 = branco | 41 = vermelho | 42 = verde | 43 = amarelo | 44 = azul | 45 = roxo | 46 = azul claro | 47 = cinza
#FORMATAÇÃO:
    # \033[m (colocar código entre o primeiro colchete e "m"
    # Separar os códigis usando ponto e vírgula ";"
    # EX: \033[0;33;44m
    #Nesse EX: style = 0 = none | text = 33 = amarelo | back = 44 = azul

###################################################################################

print('\033[0;30;107mOlá, mundo!\033[m')
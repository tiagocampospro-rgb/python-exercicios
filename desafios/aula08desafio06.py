#Faça um programa em python que abra e reproduza o áudio de um arquivo mp3. (colocarei uma música autoral minha)
import pygame # type: ignore
pygame.init()
pygame.mixer.music.load('Colorindo_o_ceu.mp3')
pygame.mixer.music.play()
pygame.event.wait()
#Seguindo por esse código deu problema, mas com o chatgpt cheguei na solução e está rodando normalmente na pasta 'aula008desafio6tent2
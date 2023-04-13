print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 58 '}\033[1;33m{'='*30}\033[m")
# importar a biblioteca
import random
import pygame
from time import sleep
import pyautogui as pt
pygame.mixer.init()
lista = ['1','2','3','4','5']

# random
r = random.randint(1,5)
# coletar os dados
n = input('\033[1;33m->\033[m Digite um número de 1 a 5: ')
    # caso de apertar uma opção inválida
while n.isnumeric() ==  False or n not in lista:
    pygame.mixer.music.load('../../sounds/pum.mp3')
    pygame.mixer.music.play()
    n = input('\033[1;31mXXX\033[m Digite uma opção válida! ')
n = int(n)
# tente novamente
while n != r:
    pygame.mixer.music.load('../../sounds/errou.mp3')
    pygame.mixer.music.play()
    print('\033[31mErrouuuuu!\033[m')
    r = random.randint(1, 5)
    n = input('\033[1;33m->\033[m Tente novamente: ')
    while n.isnumeric() == False or n not in lista:
        pygame.mixer.music.load('../../sounds/pum.mp3')
        pygame.mixer.music.play()
        n = input('\033[1;31mXXX\033[m Digite uma opção válida! ')
    n = int(n)
n = int(n)
# caso acertou
if n == r:
    pygame.mixer.music.load('../../sounds/ohyeah.mp3')
    pygame.mixer.music.play()
    print('\033[32mAcertou!')
print(f"\033[1;33m{'=' * 73}\033[m")
cont = str(input('Gostaria de continuar? \033[1;34m[s/n]\033[m ')).lower()
while cont not in 'sn':
    cont = input('\033[1;31mXXX\033[m Digite uma opção válida! ')
if cont == 's':
    print('\033[36mREINÍCIO EM ...\033[m')
    sleep(0.5)
    for c in range(4,-1,-1):
        print(c)
        sleep(0.3)
    pt.hotkey('Shift','F10')*2
elif cont == 'n':
    print(f'\033[35m\U0001F625 \033[m Então você não gosta de mim \033[35m\U0001F625 \033[m')
input()
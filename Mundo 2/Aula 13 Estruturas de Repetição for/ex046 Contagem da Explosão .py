
print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 46 '}\033[1;33m{'='*30}\033[m")
# importa time
import pygame
from time import sleep
print('\033[1;33m->\033[m Contagem regressiva: ')
# criar uma estrutura de repetição
for c in range(10,-1,-1):
    if c % 2 == 0:
        print('\033[36m',c,'\033[m', end='')
        sleep(0.5)
    else:
        print('\033[32m', c, '\033[m', end='')
        sleep(0.5)
print('\n')
# emoji
fogos = '\U0001F386'
# printar
print(f"            \033[m \033[31m{fogos*3} \033[33m{fogos*3}\033[1;35m FELIZ ANO NOVO!\033[m  \033[33m{fogos*3} \033[31m{fogos*3}")

# som de explosão
pygame.mixer.init()
pygame.mixer.music.load('../../sounds/bum.mp3')
pygame.mixer.music.play()


print(f"\033[1;33m{'=' * 73}\033[m")
input()
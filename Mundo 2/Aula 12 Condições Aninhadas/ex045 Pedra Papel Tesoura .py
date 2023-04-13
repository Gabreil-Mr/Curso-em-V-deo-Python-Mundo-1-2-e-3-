print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 44 '}\033[1;33m{'='*30}\033[m")
import pyautogui as pt
from time import sleep
import pygame
pygame.mixer.init()
pt.click(240, 930)
# jogada da pessoa
pes = int(input("""O que você escolhe:
\033[1;36m( 1 )\033[m Pedra
\033[1;36m( 2 )\033[m Papel
\033[1;36m( 3 )\033[m Tesoura
\033[1;31m * \033[m"""))
sleep(1)
pt.click(240, 930)

# jogada do computador
import random
lista = ['pedra','papel','tesoura']
comp = random.choice(lista)
print(f'COMPUTADOR: {comp}')
# trantando a jogada da pessoa
if pes == 1:
   pes = 'pedra'
   print('VOCÊ: Pedra')
elif pes == 2:
    pes = 'papel'
    print('VOCÊ: Papel')
elif pes == 3:
    pes = 'tesoura'
    print('VOCÊ: Tesoura')
else:
    print(f'{pes} é uma opção não válida, digite 1, 2 ou 3')
# condições
# pedra
if pes == 'pedra':
    if comp == 'pedra':
        print('\033[1;33m->\033[m \033[1;33mEmpate!\033[m')
        pygame.mixer.init()
        pygame.mixer.music.load('../../sounds/zapzap.mp3')
        pygame.mixer.music.play()

    elif comp == 'papel':
        print('\033[1;33m->\033[m Você \033[1;31mPerdeu\033[m!')
        print('Papel embrulha a Pedra')
        pygame.mixer.init()
        pygame.mixer.music.load('../../sounds/pum.mp3')
        pygame.mixer.music.play()
    else:
        print('\033[1;33m->\033[m Você \033[1;32mGanhou\033[m!')
        print('Pedra quebra Tesoura')
        pygame.mixer.init()
        pygame.mixer.music.load('../../sounds/uau.mp3')
        pygame.mixer.music.play()

# papel
if pes == 'papel':
    if comp == 'papel':
        print('\033[1;33m->\033[m \033[1;33mEmpate!\033[m')
        pygame.mixer.init()
        pygame.mixer.music.load('../../sounds/zapzap.mp3')
        pygame.mixer.music.play()
    elif comp == 'tesoura':
        print('\033[1;33m->\033[m Você \033[1;31mPerdeu\033[m!')
        print('Tesoura corta Papel')
        pygame.mixer.init()
        pygame.mixer.music.load('../../sounds/pum.mp3')
        pygame.mixer.music.play()
    else:
        print('\033[1;33m->\033[m Você \033[1;32mGanhou\033[m!')
        print('Papel embrulha Pedra')
        pygame.mixer.init()
        pygame.mixer.music.load('../../sounds/uau.mp3')
        pygame.mixer.music.play()

# tesoura
if pes == 'tesoura':
    if comp == 'tesoura':
        print('\033[1;33m->\033[m \033[1;33mEmpate!\033[m')
        pygame.mixer.init()
        pygame.mixer.music.load('../../sounds/zapzap.mp3')
        pygame.mixer.music.play()
    elif comp == 'pedra':
        print('\033[1;33m->\033[m Você \033[1;31mPerdeu\033[m!')
        print('Pedra quebra Tesoura')
        pygame.mixer.init()
        pygame.mixer.music.load('../../sounds/pum.mp3')
        pygame.mixer.music.play()
    else:
        print('\033[1;33m->\033[m Você \033[1;32mGanhou\033[m!')
        print('Tesoura corta Papel')
        pygame.mixer.init()
        pygame.mixer.music.load('../../sounds/uau.mp3')
        pygame.mixer.music.play()

print(f"\033[1;33m{'=' * 73}\033[m")
resposta = input('Quer continuar? [s/n] ')
if resposta == 's':
    print('\033[36mREINÍCIO EM ...\033[m')
    for c in range(4, -1, -1):
        print(c)
        sleep(0.7)
    pt.hotkey('Shift', 'F10') * 2
elif resposta == 'n':
    print('Você não deve gostar de brincar comigo (-_-) ')
else:
    print('opção inválida')
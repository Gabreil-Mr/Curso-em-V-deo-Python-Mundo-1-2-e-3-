print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 68 '}\033[1;33m{'='*30}\033[m")
import random
import pygame
pygame.init()

while True:
    print('\033[1;34m=-'*4,'\033[1;36mPAR OU ÍMPAR\033[m','\033[1;34m=-\033[m'*4)

# número
    n = input('Digite um valor de 0 a 5: ')
    while n.isnumeric() == False or int(n)>5:
        print('\033[1;31mXXX\033[m Opção não válida!')
        pygame.mixer.music.load('../../sounds/pum.mp3')
        pygame.mixer.music.play()
        n = input('Digite novamente: ')
    n = int(n)

# jogador
    jog = input('Par ou Ímpar? \033[1;35m[p/i]\033[m ')
    while jog not in 'iIpP':
        print('\033[1;31mXXX\033[m Opção não válida!')
        pygame.mixer.music.load('../../sounds/pum.mp3')
        pygame.mixer.music.play()
        jog = input('Digite novamente: ')
    jog = str(jog).lower()

    print('\033[1;34m=-'*15,'\033[m')

# computador
    comp = random.randint(0,5)

# jogadas
    print(f'\033[1;33m->\033[m O \033[1mplayer\033[m jogou: \033[1;34m{n}\033[m \n\033[1;33m->\033[m O \033[1mcomputador\033[m jogou: \033[1;34m{comp}\033[m')
    print(f'{n} + {comp} = {n+comp}')
# caso par
    if jog == 'p':
        if ((n+comp) % 2) == 0:
            print('Você \033[1;32mVENCEU\033[m!')
            pygame.mixer.music.load('../../sounds/uau.mp3')
            pygame.mixer.music.play()
        else:
            print('Você \033[1;31mPERDEU\033[m!')
            pygame.mixer.music.load('../../sounds/errou.mp3')
            pygame.mixer.music.play()
# caso impar
    if jog == 'i':
        if ((n + comp) % 2) != 0:
            print('Você \033[1;32mVENCEU\033[m!')
            pygame.mixer.music.load('../../sounds/uau.mp3')
            pygame.mixer.music.play()
        else:
            print('Você \033[1;31mPERDEU\033[m!')
            pygame.mixer.music.load('../../sounds/errou.mp3')
            pygame.mixer.music.play()

    print(f"\033[1;33m{'=' * 73}\033[m")
# continuar
    cont = str(input('Gostaria de continuar? \033[1;35m[s/n]\033[m ')).lower()
    while cont not in 'sn':
        print('\033[1;31mXXX\033[m Digite uma opção válida! ')
        pygame.mixer.music.load('../../sounds/pum.mp3')
        pygame.mixer.music.play()
        cont = str(input('Gostaria de continuar? \033[1;35m[s/n]\033[m ')).lower()
    if cont == 's':
        print('Okay!')
        n = 1
    elif cont == 'n':
        print(f'\033[35m\U0001F625 \033[m Então você não gosta de mim \033[35m\U0001F625 \033[m')
        break
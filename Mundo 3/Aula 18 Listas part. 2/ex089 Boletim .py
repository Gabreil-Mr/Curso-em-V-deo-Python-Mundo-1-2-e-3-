print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 89 '}\033[1;33m{'='*30}\033[m")
import pygame
pygame.mixer.init()
lista = []
boletim = []
cont = 0
print('\033[1;31mBOLETIM DO GROSSO\033[m')
print('-'*20)
while True:
    lista.append(input('Nome: '))
    x = float(input('Nota 1: '))
    lista.append(x)
    y = float(input('Nota 2: '))
    lista.append(y)
    boletim.append(lista[:])
    lista.clear()
    print('-' * 20)
    a = input('Quer continuar? [s/n] ')
    if a in 'Nn':
        break
    elif a in 'Ss':
        print('-'*20)
    else:
        pygame.mixer.music.load('../../sounds/bum.mp3')
        pygame.mixer.music.play()

print('-='*12)
print('Nº  Nome          Média')
print('-'*24)
for aluno in boletim:
    cont += 1
    print(f"{cont}{' ':^3}{aluno[0]}{' ' * (14 - len(aluno[0]))}{(x+y)/2}")
print('-='*12)
while True:
    num = int(input('Digite o número do aluno para ver a nota completa: '))
    num -= 1
    print(f"Aluno: {boletim[num][0]}  "
          f"Nota 1: {boletim[num][1]} "
          f"Nota 2: {boletim[num][2]}")
    a = input('Quer continuar? [s/n] ')
    if a in 'Nn':
        break
    elif a in 'Ss':
        print('-' * 20)
    else:
        pygame.mixer.music.load('../../sounds/bum.mp3')
        pygame.mixer.music.play()

print(f"\033[1;33m{'=' * 73}\033[m")
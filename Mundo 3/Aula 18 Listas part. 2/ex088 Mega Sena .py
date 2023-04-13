print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 87 '}\033[1;33m{'='*30}\033[m")
from random import randint
lista = []
print('\033[1m-\033[m'*35)
print(' '*11,'MEGA SENA')
print('\033[1m-\033[m'*35)
while True:
    quanJ = input('Quantos jogos quer jogar? ')
    if quanJ.isnumeric() == True:
        quanJ = int(quanJ)
        break
    else:
        print('\033[1;31mXXX\033[m Digite uma opção válida!')
print('=-'*3,'Carregando os jogos','=-'*3)
for jogo in range(0,quanJ):
    for num in range(0,6):
        lista.append(randint(0,60))
    print(f'Jogo {jogo+1}: ',end='')
    for num in lista:
        print(num,end=' ')
    print()
    lista.clear()
print('=-'*5,'Boa Sorte!','=-'*5)
print(f"\033[1;33m{'=' * 73}\033[m")
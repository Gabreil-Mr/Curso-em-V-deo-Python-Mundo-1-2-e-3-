print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 91 '}\033[1;33m{'='*30}\033[m")
from random import randint
from time import sleep

# num jogadores
numjog = int(input("Quantos jogadores vão participar? "))

# sorteio dos dados
rank = {}
for c in range(0,numjog):
    rank[f"Jogador{c+1}"] = randint(0, 6)
print("\033[1;31m-\033[m"*30)

#exposição do sorteio
for k,v in rank.items():
    print(f"\033[1;34m{k}\033[m tirou \033[1;32m{v}\033[m no dado.")
    sleep(0.8)
print("\033[1;31m-\033[m"*30)

# Organizando o ranking
print("-="*5,"RANKING","-="*5)
for i,v in enumerate(sorted(rank.items(), key=lambda item:item[1], reverse=True)): #por que usar key=lamba envés de ,values?
    print(f"\033[1;31 m     {i+1}º)\033[1;34m {v[0]}\033[m com \033[1;32m{v[1]}\033[m")
    sleep(0.5)

# outra forma de fazer

players = dict()
print('Drawn values: ')
for play in range(1, 5):
    players[f'player{play}'] = randint(1, 6)
    print(f'    Player {play} rolled {players[f"player{play}"]}')
    sleep(0.5)
print('Player ranking')
for key, value in enumerate(sorted(players, key=players.get, reverse=True)):
    print(f'    {key + 1}° place: {value} with {players[value]}')
    sleep(0.5)

print(f"\033[1;33m{'=' * 73}\033[m")
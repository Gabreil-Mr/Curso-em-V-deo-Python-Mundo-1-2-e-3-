print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 74 '}\033[1;33m{'='*30}\033[m")
from random import randint
maior = 0
menor = 101
print('\033[1;35m->\033[m Lista de Valores:  ', end='')
for letra in ('a','b','c','d','e'):
    letra = randint(0,101)
    print(f'\033[34m{letra}\033[m', end='  ')
    if letra > maior:
        maior = letra
    if letra < menor:
        menor = letra
print('')
# também era possivel faze usando o max e min, mas pra isso precisaria criar uma nova lista
print(f'\033[1;35m->\033[m O maior valor: \033[34m{maior}\033[m')
print(f'\033[1;35m->\033[m O menor valor: \033[34m{menor}\033[m')

print(f"\033[1;33m{'=' * 73}\033[m")

from random import sample

a = tuple(sample(range(10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')
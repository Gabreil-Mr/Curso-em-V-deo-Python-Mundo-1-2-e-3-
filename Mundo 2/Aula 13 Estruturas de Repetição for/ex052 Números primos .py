print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 52 '}\033[1;33m{'='*30}\033[m")

# coletando o numero
n = input('Digite um número: ')
    # caso seja escrito errado
import pyautogui as pt
from time import sleep

isn = n.isnumeric()
if isn == True:
    n = int(n)
else:
    print(f'\033[1;34m {n}\033[m não é um \033[4mnúmero inteiro\033[m')
    sleep(1)
    print('\033[36mREINÍCIO DO PROGRAMA EM ...\033[m')
    for c in range(4, -1, -1):
        print(c)
        sleep(0.7)
    pt.hotkey('Shift', 'F10') * 2
# os divisores de n
div = 0
for c in range(1,n+1):
    if n % c == 0:
        div += 1
        print('\033[1;31m{}\033[m'.format(c),end=' ')
    else:
        print('\033[1;33m{}\033[m'.format(c),end=' ')
# resultado final
if div==2:
    print(f'\n\033[1;35m-> \033[m\033[34m{n}\033[m é \033[32msim\033[m primo, pois possui 2 divisores')
else:
    print(f'\n\033[1;35m-> \033[m\033[34m{n} \033[31mnão\033[m é um primo, pois não exatamente possui 2 divisores')

print(f"\033[1;33m{'=' * 73}\033[m")
print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 59 '}\033[1;33m{'='*30}\033[m")
import math
import pyautogui as pt
from time import sleep
# lista de opções:
lista = ['-1','0','1','2','3','4','5','6']
op = ''
# 1) coletando os valores
print('Digite os valores')
x = float(input( ' x = '))
y = float(input(' y = '))
    # ideia: fazer com que seja possivel colocar operações
# 2) operações
    # opções
while op != -1:
    op = input('''Selecione a operação:
\033[1;34m[ 1 ]\033[m soma                    \033[1;34m[ 4 ]\033[m diferença  
\033[1;34m[ 2 ]\033[m multiplicação           \033[1;34m[ 5 ]\033[m divisão          
\033[1;34m[ 3 ]\033[m potência                \033[1;34m[ 6 ]\033[m raiz quadrada 
\033[1;34m{-1 }\033[m fechar programa ------- \033[1;34m{ 0 }\033[m novos números
\033[1;31m * \033[m ''''')
    if op not in lista:
        print('Opção não válida')
        sleep(2)
        print('\033[36mREINÍCIO EM ...\033[m')
        for c in range(4, -1, -1):
            print(c)
            sleep(0.7)
        pt.hotkey('Shift', 'F10') * 2
    op = int(op)
    # resultado
    if op == 1:
        print(f'\033[1;33m->\033[m {x} + {y} = {x+y}')
    elif op == 2:
        print(f'\033[1;33m->\033[m {x} x {y} = {x+y}')
    elif op == 3:
        print(f'\033[1;33m->\033[m {x}^{y} = {math.pow(x,y)} / {x}^{y} = {math.pow(y,x)}')
    elif op == 4:
        print(f'\033[1;33m->\033[m {x} - {y} = {x-y} / {y} - {x} = {y-x}')
    elif op == 5:
        print(f'\033[1;33m->\033[m {x} % {y} = {x/y} / {y} % {x} = {x/y}')
    elif op == 6:
        print(f'\033[1;33m->\033[m √{x} = {math.sqrt(x)} / √{y} = {math.sqrt(y)}')
    elif op == 0:
        x = float(input('x = '))
        y = float(input('y = '))
    sleep(3)
    print(f"\033[1;33m{'=' * 73}\033[m")

print(f"\033[35mTchau!\033[m")
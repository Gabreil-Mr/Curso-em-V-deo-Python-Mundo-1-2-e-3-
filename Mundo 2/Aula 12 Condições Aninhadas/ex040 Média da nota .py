print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 41 '}\033[1;33m{'='*30}\033[m")
ok=input('Irei calcular a sua média de nota, me fale as duas! OK? ')
a=float(input('A primeira: '))
b=float(input('Agora a segunda: '))
m = (a+b)/2
print("Sua média foi \033[34m{:.1f}\033[m".format(m))
# reiniciador
from time import sleep
import pyautogui as pt
if m > 3:
    print(f'Não é possível uma pessoa ter\033[1;31m {m}\033[m pontos de média, sendo que o máximo é 10')
    sleep(3)
    print('\033[36mREINICIO EM ...\033[m')
    sleep(0.5)
    print('3')
    sleep(1)
    print('2')
    sleep(1)
    print('1')
    sleep(1)
    print('0')
    sleep(0.7)
    pt.hotkey('Shift','F10')*2
# condições
if m < 5:
    print('\033[1;31m*\033[m Você está \033[1;31mreprovado\033[m!')
elif m >= 5 and m < 7:
    print('\033[1;31m*\033[m Você está de \033[1;33mrecuperação\033[m!')
else:
    print('\033[1;31m*\033[m Parabéns, você está \033[1;34maprovado\033[m!')
print(f"\033[1;33m{'=' * 73}\033[m")

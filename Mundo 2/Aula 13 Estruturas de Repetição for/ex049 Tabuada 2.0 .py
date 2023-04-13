print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 49 '}\033[1;33m{'='*30}\033[m")
#importar a bibliotecas
import pyautogui as pt
from time import sleep
#coletar a váriavel
print('\033[1;31mTABUADA 2.0\033[m')
n = input('Digite um número inteiro: ')
# reiniciar o programa se o número digitado não for int
isn = n.isnumeric()
if isn==True:
    n= int(n)
else:
    print('\033[1;33m->\033[m Você não digitou um \033[4mnúmero inteiro\033[m')
    sleep(1)
    print('\033[36mREINÍCIO DO PROGRAMA EM ...\033[m')
    for c in range(4, -1, -1):
        print(c)
        sleep(0.7)
    pt.hotkey('Shift', 'F10') * 2
#fazer a estrutura da tabuada
print('\033[1;35m=-=-\033[m'*6)
for c in range(1,11):
    print("\033[31m    {}\033[33m * \033[31m{}\033[m = \033[34m{:0>2}\033[m".format(c,n,c*n))
print('\033[1;35m=-=-\033[m'*6)


print(f"\033[1;33m{'=' * 73}\033[m")

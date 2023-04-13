print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 43 '}\033[1;33m{'='*30}\033[m")
import pyautogui as pt
from time import sleep
# tirar o peso e altura
peso = float(input("Qual é o seu peso atual? \033[31mKG\033[m: "))
altu = str(input('Qual a sua altura? \033[31mMetros\033[m:  '))
#tratando o peso no caso de ,
if altu.find('.') > 0:
    altu.replace(',','.')
altu = float(altu)
#tratando o peso no case de cm
if altu > 20:
    altu = altu / 100
    print(f'Pelo visto você colocou em cm, porque não é possivel uma pessoa ter {altu*100} m. \nEntão...')
# reinicio no caso de uma altura inimaginável
if altu > 3:
    print(f'Não é possível uma pessoa ter\033[1;31m {altu} METROS\033[m')
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
# realizar o imc
imc = peso/(altu**2)
print("\033[33m<*>\033[m Seu IMC é de \033[34m{:.1f}\033[m".format(imc))
# condição
if imc < 18.5:
    print('\033[1;31m*\033[m Condição: \033[1;33mAbaixo do Peso\033[m ')
elif imc <= 25:
    print('\033[1;31m*\033[m Condição: \033[1;33mPeso Ideal\033[m')
elif imc <= 30:
    print('\033[1;31m*\033[m Condição: \033[1;33mSobrepeso\033[m')
elif imc <= 40:
    print('\033[1;31m*\033[m Condição: \033[1;33mObesidade\033[m')
else:
    print('\033[1;31m*\033[m Condição: \033[1;33mObesidade Mórbida\033[m')
print(f"\033[1;33m{'=' * 73}\033[m")
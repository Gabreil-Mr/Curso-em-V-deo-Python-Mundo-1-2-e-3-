print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 44 '}\033[1;33m{'='*30}\033[m")
import pyautogui as pt
from time import sleep
# pegar o preço
val = float(input('Qual é o valor do produto? \033[31mR$:\033[m '))
   # formatação do preço
   #valf = ('\033[31mR$:{:.2f}\033[m'.format(val))
# opção de pagamento
pag = int(input("""
Selecione a opção de pagamento:
(promoção à vista em qualquer tipo de pagamento)
\033[1;36m[ 1 ]\033[m Dinheiro ou Cheque
\033[1;36m[ 2 ]\033[m Cartão crédito/débito
\033[1;31m * \033[m"""))
#print('\n')
# preço final
# dinheiro ou cartão
if pag == 1:
    val = val - (val/10)
    print('\033[33m->\033[m Você escolheu \033[4;34mdinheiro\033[m')
    print('Com dinheiro/cheque à vista você ganha um \033[4mdesconto de 10%\033[m')
    print('O preço final é de \033[32mR$:{:.2f}\033[m'.format(val))
# crédito ou débito
elif pag == 2:
    a = int(input("""\033[1;33m{ 1 }\033[m Crédito ou \033[1;33m{ 2 }\033[m Débito? 
\033[1;31m * \033[m """))
    # débito
    if a == 2:
        val = val - val/10
        print('\033[33m->\033[m Você escolheu \033[4;34mdébito\033[m')
        print('Com cartão de débito à vista você ganha um \033[4mdesconto de 10%\033[m')
        print('O preço final é de \033[32mR$:{:.2f}\033[m'.format(val))
    # crédito
    elif a == 1:
        print('\033[33m->\033[m Você escolheu \033[4;34mcrédito\033[m')
        ba = int(input("""Em quantas parcelas prentende pagar?     
  \033[1;36m( 1 )\033[1m \033[m1x\033[m À vista: \033[1m5% de desconto\033[m
  \033[1;36m( 2 )\033[1m \033[m2x \033[mno cartão: \033[1mpreço normal\033[m
  \033[1;36m( 3 )\033[1m \033[m3x \033[mno cartão: \033[1m20% de juros\033[m
  \033[1;33m< * >\033[m Não aceitamos mais parcelas
\033[1;31m* \033[m """))
        # parcelas
        if ba == 1:
            val = val - ((val*5)/100)
            val = '\033[1;32mR$: {:.2f}\033[m'.format(val)
            print(f' O preço final é de {val}')
        elif ba == 2:
            val = (val - ((val * 5) / 100))/2
            val = '\033[1;32mR$: {:.2f}\033[m'.format(val)
            print(f' O preço final é de {val} \033[4mp/mês\033[m')
        elif ba == 3:
            val = (val - ((val * 5) / 100)) / 3
            val = '\033[1;32mR$: {:.2f}\033[m'.format(val)
            print(f'O preço final é de {val} \033[4mp/mês\033[m')
          #opção não válida
        else:
            print(f'\033[1;31m {ba} \033[mé uma opção não válida')
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
            pt.hotkey('Shift', 'F10') * 2
    else:
        print(f'\033[33m->\033[m \033[1;31m {a} \033[mé uma opção não válida')
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
        pt.hotkey('Shift', 'F10') * 2
else:
    print(f'\033[33m->\033[m \033[1;31m {pag} \033[mé uma opção não válida')
    sleep(3)
    print('\033[36mREINICIO EM ...\033[m')
    sleep(0.5)
    print('3')
    sleep(1)
    print('2')
    sleep(1)
    print('1')
    sleep(1)
    print('\033[1;36m0\033[m')
    sleep(0.7)
    pt.hotkey('Shift', 'F10')*2

print(f"\033[1;33m{'=' * 73}\033[m")
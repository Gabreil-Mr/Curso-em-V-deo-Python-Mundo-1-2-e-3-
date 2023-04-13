print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 72 '}\033[1;33m{'='*30}\033[m")

numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
           'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito'
           ,'dezenove','vinte')

while True:
    num = input('Digite um número entre 0 e 20: ')
    if num.isnumeric() == True and 0 <= int(num) <= 20:
       num = int(num)
       break
    print('\033[1;31mXXX\033[m Digite uma opção válida! ')

print(f'\033[1;33m->\033[m Você digitou o número \033[1;34m{numeros[num]}\033[m')

print(f"\033[1;33m{'=' * 73}\033[m")
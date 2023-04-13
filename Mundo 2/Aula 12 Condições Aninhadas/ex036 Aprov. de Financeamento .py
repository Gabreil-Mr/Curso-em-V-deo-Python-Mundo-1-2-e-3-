print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 36 '}\033[1;33m{'='*30}\033[m")
ola = input('Olá, tudo bem? ').lower()
if ola in 'não nao na n no':
    print('Então \033[1;31mSAIA DAQUI\033[m, você precisa estar bem para fazer um empréstimo.')
else:
    nome = str(input('\033[1;31m*\033[m Poderia me dizer o seu nome? ')).title()
    print(f'{nome}, este é um programa que irá analisar se você está apto a realizar o financeamento de uma casa.'
                '\nResponda as perguntas abaixo por favor: ')
    casa = float(input('\033[1;31m*\033[m Qual o valor da casa? \033[1;32mR$:\033[m'))
    sal = float(input('\033[1;31m*\033[m Qual o valor de seu salário? \033[1;32mR$:\033[m'))
    anos = float(input('\033[1;31m*\033[m Em quantos anos vai pagar? '))
    prest = casa / (anos * 12)
    if prest <= 0.3 * sal:
        print(f'\033[1;34mSerá possivel\033[m fazer o financeamento, e o valor será de \033[1;32mR$:{prest:.2f}\033[m \033[4mp/mês\033[m')
    else:
        print(f'Infelizmente \033[1;31mnão será possivel\033[m realizar o empréstimo')
print(f"\033[1;33m{'-'*73}\033[m")

# emp = float(input('\033[1;31m*\033[m Digite o valor que você planeja para o empréstimo \033[1;32mR$:\033[m'))
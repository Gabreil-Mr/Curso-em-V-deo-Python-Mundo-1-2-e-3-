print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 38 '}\033[1;33m{'='*30}\033[m")
# inputs
a = float(input('Digite um número: '))
b = float(input('Digite outro: '))
# condições
if a < b:                    # b como maior
    print(f'\033[1;31m*\033[m o segundo \033[34m({b})\033[m é o \033[4mmaior\033[m valor')
elif b > a:                  # a como maior
    print(f'\033[1;31m*\033[m o primero \033[m{a}\033[m é o \033[mmaior\033[m valor')
else:                        # iguais
    print('\033[1;31m*\033[m \033[34mnão existe maior\033[m valor, os dois são \033[4miguais\033[m')
print(f"\033[1;33m{'=' * 73}\033[m")

# idéias extras: 1) poder comparar operações
#                2) poder comparar operações algébricas
#                3) alertar que o que está sendo colocado não é um número




















# tipos primitivos, não deu certo
f='''tipa = type(a)
if tipa == float:
    print(f'O número {a} digitado é Racional')
elif tipa == int:
    print(f'O número {a} digitado é Inteiro')
else:
    print((f'{a} NÃO É UM NÚMERO!'))
tipb = type(b)
if tipb == float:
    print(f'O número {b} digitado é Racional')
elif tipb == int:
    print(f'O número {b} digitado é Inteiro')
else:
    print((f'{b} NÃO É UM NÚMERO!'))'''

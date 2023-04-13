print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 39 '}\033[1;33m{'='*30}\033[m")
# Conseguir o ano atual
from datetime import date
ano = date.today().year
# conseguir a idade
nas = int(input('Qual é o seu ano de nascimento? '))
idade = ano - nas
print(f'Se você nasceu em \033[1;34m{ano} \033[mentão possui \033[1;34m{idade}\033[m anos hoje')
# Condições
if idade == 18:
    print('\033[1;31m*\033[m Você deve se alistar esse ano')
elif idade < 18:
    if idade == 17:
       print(f'\033[1;31m*\033[m Falta então \033[1;34m{18 - idade}\033[m ano para você se alistar')
    else:
        print(f'\033[1;31m*\033[m Faltam então \033[1;34m{18 - idade}\033[m anos para você se alistar')
elif idade > 18:
    if idade == 19:
       print(f'\033[1;31m*\033[m Já se passou \033[1;34m{idade - 18}\033[m ano desde a sua idade de alistamento')
    else:
        print(f'\033[1;31m*\033[m Já se passou \033[1;34m{idade - 18}\033[m ano desde a sua idade de alistamento')
# fim
print(f"\033[1;33m{'=' * 73}\033[m")

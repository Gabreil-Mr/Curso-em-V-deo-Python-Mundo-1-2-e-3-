print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 54 '}\033[1;33m{'='*30}\033[m")
maior = 0
menor = 0
# ano atual
from datetime import date
ano = date.today().year

for c in range(1,6):
    nas = input(f'Em que ano a {c}º pessoa nasceu? ')
    # caso coloquem o ano errado
    isn = nas.isnumeric()
    if isn == False:
        print(f'\033[1;31mXXX \033[m{nas} não é ano \033[1;31mXXX \033[m')
        nas = 0
    else:
        nas = int(nas)
    # condições finais
        if (ano - nas) < 18:
            menor += 1
        elif (ano - nas) > 18:
            maior += 1
            if (ano - nas) > 130:
                print('\033[35mhummm... SUSPEITO\033[m')

print(f'\n\033[1;33m-> \033[34m{maior}\033[m pessoas são maiores de 18 anos')
print(f'\033[1;33m-> \033[34m{menor}\033[m pessoas são menores de 18 anos')
print(f"\033[1;33m{'=' * 73}\033[m")
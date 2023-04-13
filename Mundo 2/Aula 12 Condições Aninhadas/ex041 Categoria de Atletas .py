print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 41 '}\033[1;33m{'='*30}\033[m")
#proposta
print('Este é um programa que mostra a categoria de um atleta de natação de acordo com a idade')
#conseguir a idade do atleta
from datetime import date
ano = date.today().year
idade = int(input('Digite o ano de nascimento: '))
idade = ano - idade
#condições
if idade <= 9:
    print(f'\033[1;31m*\033[m O atleta tem \033[34m{idade} \033[manos, categoria: \033[1;32mMIRIM\033[m')
elif idade <= 14:
    print(f'\033[1;31m*\033[m O atleta tem \033[34m{idade}\033[m anos, categoria: \033[1;32mINFANTIL\033[m')
elif idade <= 19:
    print(f'\033[1;31m*\033[m O atleta tem \033[34m{idade}\033[m anos, categoria: \033[1;32mJÚNIOR\033[m')
elif idade <= 24:
    print(f'\033[1;31m*\033[m O atleta tem \033[34m{idade}\033[m anos, categoria: \033[1;32mSÊNIOR\033[m')
# easter egg
elif idade > 100:
    print(f'\033[1;31m*\033[m O atleta tem \033[34m{idade}\033[m anos, categoria: \033[1;31mNADADOR DO RIO ESTIGE\033[m')
else:
    print(f'\033[1;31m*\033[m O atleta tem \033[34m{idade}\033[m anos, categoria: \033[1;32mMASTER\033[m')
print(f"\033[1;33m{'=' * 73}\033[m")



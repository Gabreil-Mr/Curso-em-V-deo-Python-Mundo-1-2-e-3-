print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 37 '}\033[1;33m{'='*30}\033[m")
print('\033[1;35m                       ~-~ \033[1mConversor de bases\033[1;35m ~-~\033[m')
n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
\033[1;33m[ 1 ]\033[m para \033[34mBINÁRIO\033[m
\033[1;33m[ 2 ]\033[m para \033[34mOCTAL\033[m 
\033[1;33m[ 3 ]\033[m para \033[34mHEXADECIMAL\033[m ''')
ba = int(input('Base escolhida: '))
if ba == 1:
    print(f"\033[1;31m*\033[m O número \033[32m{n}\033[m em \033[34mBinário\033[m fica \033[32m{bin(n).replace('0b','')}\033[m")
elif ba == 2:
    print(f"\033[1;31m*\033[m O número \033[32m{n}\033[m em \033[34mOctal\033[m fica \033[32m{oct(n).replace('0o','')}\033[m")
elif ba == 3:
    print(f"\033[1;31m*\033[mO número \033[32m{n}\033[m em \033[34mHexadecimal\033[m fica \033[32m{hex(n).replace('0x','')}\033[m")
else:
    print('Opção invalida, tente novamente!')
print(f"\033[1;33m{'=' * 73}\033[m")


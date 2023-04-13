print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 42 '}\033[1;33m{'='*30}\033[m")

print('Digite o valor dos segmentos para ver se eles formam um triângulo')
a = float(input('O primeiro: '))
b = float(input('O segundo: '))
c = float(input('O terceiro: '))
lista = [a,b,c]
lista = sorted(lista)
if lista[0] + lista[1] > lista[2]:
    print('\033[1;31m*\033[m Os segmentos formam \033[1;32msim\033[m um triângulo')
    if lista[0] == lista[1] and lista[0]!= lista[2] or lista[1] == lista[2] and lista[1] != lista[0]:
        print('\033[1;31m~\033[m O triângulos é \033[4;34misóceles\033[m')
    elif lista[0] == lista[1] == lista[2]:
        print('\033[1;31m~\033[m O triângulo é \033[4;35mequilátero\033[m')
    else:
        print('\033[1;31m~\033[m O triângulo é \033[4;36mescaleno\033[m')
        # easter egg
        if (lista[0]+lista[1]+lista[2])%12==0:
            print('\033[36m+++++ TRIÂNGULHO PITAGÓRICO +++++\033[m+')
else:
    print('\033[1;31m*\033[m Os Segmentos \033[1;31mnão\033[m formam um triângulo')
print(f"\033[1;33m{'=' * 73}\033[m")

print('='*20,'DESAFIO 32','='*20)
ano = int(input('Informe-me um ano e direi se ele é bissexto: '))
print(f'O ano colocado foi {ano}')
if ano/4 == ano//4:
    if (ano/100 != ano//100):
        print('Esse é um ano bissexto')
    else:
        if ano/400 == ano//400:
            print('Esse é um ano bissexto')
        else:
            print('Esse não é um ano bissexto')
else:
    print('Esse ano não é bissexto')

# Forma como o Guanabara resolveu:
import datetime
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = ano.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')
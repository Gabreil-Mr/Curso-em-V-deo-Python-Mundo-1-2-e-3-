print('='*22,'DESAFIO 35','='*22)
print('Digite o valor dos segmentos para ver se formam um triângulo')
a = float(input('O primeiro: '))
b = float(input('O segundo: '))
c = float(input('O terceiro: '))
lista = [a,b,c]
listaO = sorted(lista)
if listaO[0] + listaO[1] > listaO[2]:
    print('Os segmentos formam um triângulo')
else:
    print('Os Segmentos não formam um triângulo')

print('\n~ Solução do Guanabara ~')

if a + b > c and a + c > b and b + c > a:
    print('Os segmentos formam um triângulo')
else:
    print('Os segmentos não formam um triângulo')

print(f"\033[1;33m{'='*22}\033[1;34m{' DESAFIO 34 '}\033[1;33m{'='*22}\033[m")

print('\nDigite 3 números ')
a = float(input('O primeiro: '))
b = float(input('O segundo: '))
c = float(input('O terceiro: '))

print('\n \033[1;34m~~~~~ Maior e menor valores ~~~~~\033[m')

print('\n\033[0;35m- Solução usando sorted() -\033[m')

lista =[a,b,c]
listaO = sorted(lista)

print(f'O menor número é {listaO[0]}')
print(f'O maior número é {listaO[2]}')

print('\n\033[0;35m- Solução usando max() e min() -\033[m')

print(f'O maior valor digitado foi {max(lista)}')
print(f'O menor numero digitado foi {min(lista)}')

print('\n\033[0;35m- Solução do Guanabara -\033[m')

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')

print('\n\033[36m~~~~~ Ordenando a sequência de valores ~~~~~\033[m' )
print('\n\033[35m- Usando Condições -\033[m')
if a > b > c:
    print(a,b,c)
if a > c > b:
    print(a,c,b)
if b > a > c:
     print(b, a, c)
if b > c > a:
    print(b, c, a)
if c > a > b:
    print(c,a,b)
if c > b > a:
    print(c,b,a)
print('\n\033[35m- Usando sorted() -\033[m')

lista =[a,b,c]
print(sorted(lista))



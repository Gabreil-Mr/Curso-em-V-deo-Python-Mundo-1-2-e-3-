print('='*20,'DESAFIO 23','='*20)
n = int(input('Digite um número de 0 a 9999: '))
print(f'''Unidade:{n // 1 % 10}
Dezena: {n // 10 % 10}
Centena: {n // 100 % 10}
Milhar: {n // 1000 % 10}''')
print( '-'*20,'DE OUTRA FORMA','-'*20)
num = str(int(n + 10000))
print(f'''Unidade: {num[4]}
Dezena: {num[3]}
Centena: {num[2]}
Milhar: {num[1]}
''')
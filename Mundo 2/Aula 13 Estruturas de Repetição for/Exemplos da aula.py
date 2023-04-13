
for c in range(9,0,-1):
    print(c)

print('\n')

ini =  int(input('Começo: '))
fim = int(input('Término: '))
pas = int(input('Passo: '))
for c in range(ini,fim+1,pas):
    print(c)
print('FIM')

print('\n')
s = 0
for c in range(0,3):
    v = int(input('Digite um valor: '))
    s += v
print(f'O somatório de todos os valores foi {s}')
print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 51 '}\033[1;33m{'='*30}\033[m")

#coletar as variáveis
p = int(input('Digite o primeiro termo: '))
r = int(input('Razão: '))
u = p + (r * 10)
for c in range(p,u+1,r):
    print(f' {c} ',end='\033[1;33m->\033[m')
print('\033[1;31m fim\033[m')

print(f"\033[1;33m{'=' * 73}\033[m")
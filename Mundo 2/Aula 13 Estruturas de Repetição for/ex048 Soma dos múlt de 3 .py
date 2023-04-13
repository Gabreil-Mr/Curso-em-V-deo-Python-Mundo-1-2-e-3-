print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 48 '}\033[1;33m{'='*30}\033[m")

print('O somatório dos múltiplos de \033[34m3 \033[m ímpares de \033[34m0\033[m a \033[34m500\033[m é: ',end='')
s=0
for c in range(0,501,3):
   if c%3==0 and c%2!=0:
        s += c
print("\033[31m{:,}\033[m".format(s))
print(f"\033[1;33m{'=' * 73}\033[m")

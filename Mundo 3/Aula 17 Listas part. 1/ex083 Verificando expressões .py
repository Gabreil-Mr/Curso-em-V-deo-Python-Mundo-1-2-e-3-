print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 83 '}\033[1;33m{'='*30}\033[m")
cont = 0
exp = input('Digite a expressão: ')

exp = exp.replace('',' ')
exp = exp.split()

for letra in exp:
    if letra == '(':
        cont += 1
    if letra == ')':
        cont -= 1
    if cont < 0:
        break
if cont == 0:
    print('( \033[1;32mO\033[m ) A expressão é válida')
elif cont != 0:
    print('( \033[1;31mX\033[m ) A expressão não é válida')

print(f"\033[1;33m{'=' * 73}\033[m")

# ideia: se eu quero fazer um programa que leia e resolva uma equação esse é um passo essencial,
# ele pode ler a equação e dizer que está errada, e oferecer a opção de corrigí-la

print(f"\033[1;36m{'-'*16}\033[m Solução Guanabara \033[1;36m{'-'*16}\033[m")
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')

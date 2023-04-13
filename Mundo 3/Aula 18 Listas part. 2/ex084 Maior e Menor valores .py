
print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 84 '}\033[1;33m{'='*30}\033[m")
print('\033[1;31mPESO ANALAISER\033[m')
dado = []
banco = []
maior = 0

# quantidade de termos com erro
while True:
    termos = input('Quantidade de pessoas: ')
    if termos.isnumeric() == True:
        termos = int(termos)
        break
    else:
        print('\033[1;31mXXX\033[m Digite uma opção válida!')

# processo de armazenagem
for c in range(0,termos):
    dado.append(input('Nome: '))
    dado.append(int(input('Peso: ')))
    if dado[1] >= maior:
        maior = dado[1]
    banco.append(dado[:])
    dado.clear()

# resultados finais
    # a) Quantidadde de pessoas
print(f'\033[1;33m->\033[m Quantidade de cadastros: \033[34m{len(banco)}\033[m')
    # b) pessoas + pesadas
conj_pes = []
a = 0
for peso in banco:
    for c in conj_pes:
        if peso[1] > c[1]:
            a += 1
    conj_pes.insert(a,peso)
    # resultado
print(f'\033[1;33m->\033[m O maior peso foi de {conj_pes}Pessoas + pesadas: ', end='')
for c in conj_pes:
    if c == conj_pes[a]:
        print(c)

print('\033[1;33m->\033[m Pessoas + leves: ', end='')
for pessoa in conj_pes[::-1]:
    print(pessoa[0],end=' ')
print('')

print(f"\033[1;33m{'=' * 73}\033[m")

# Solução Guanabara

dado = []
banco = []
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    banco.append(dado[:])
    if dado[1] >= maior:
        maior = dado[1]
    if dado[1] >= menor:
        menor = dado[1]
    dado.clear()
    cont = str(input('Quer continuar? [S/N] '))
    if cont in 'Nn':
        break
print(banco)
print('')
print(f'Quantidade de cadastros: {len(banco)}')
print(f"Maior Peso: {maior:.2f} Kg / Pessoas mais pesadas: ", end='')
for cad in banco:
    if cad[1] == maior:
        print(cad[0],end=' ')
print(f"Menor Peso: {menor:.2f} Kg / Pessoas mais leves: ", end='')
for cad in banco:
    if cad[1] == menor:
        print(cad[0],end=' ')

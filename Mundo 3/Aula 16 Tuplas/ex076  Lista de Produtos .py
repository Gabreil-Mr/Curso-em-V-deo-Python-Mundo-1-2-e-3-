print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 76 '}\033[1;33m{'='*30}\033[m")

produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

print('\033[1;35m=\033[m'*44)
print(' '*11,'Listagem de Preços')
print('\033[1;35m=\033[m'*44)
for c in produtos:
    if c == str(c):
        print(f'{c}','.'*(33-len(c)),end='')
    elif c == float(c):
        print(f' \033[32mR$:\033[m\033[1m {c:.2f}\033[m')
print('\033[1;35m=\033[m'*44)

print(f"\033[1;33m{'=' * 73}\033[m")

# solução mais enxuta

lista = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
for i in range(0,int(len(lista)),2):
    print(f'{lista[i]:.<30}R${lista[i+1]:>6.2f}')

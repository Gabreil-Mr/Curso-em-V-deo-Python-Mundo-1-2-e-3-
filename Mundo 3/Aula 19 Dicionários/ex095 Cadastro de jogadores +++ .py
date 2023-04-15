print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 95 '}\033[1;33m{'='*30}\033[m")
jog = {}
banco = []
cont = ""
num = dados = 0

#pedir as informações do jogador
while True:
    jog["cod"] = num
    num += 1
    jog["Nome"] = str(input("Nome: ")).title()
    partidas = int(input(f"Número de partidas de {jog['Nome']}: "))
    jog["Gols"] = []
    for i in range(0,partidas):
        jog["Gols"].append(int(input(f"Gols na partida {i+1}: ")))
    jog["Total"] = sum(jog["Gols"])
    print(jog)

    # armazenar cada jogardor numa lista
    banco.append(jog.copy())
    jog.clear()

    print("\033[1;31m-\033[m" * 30)

#Continuar
    while True:
        cont = str(input("Continuar? [S/N] ")).lower()
        if cont in "sn":
            break
        print("\033[1;31mXXX\033[m Por favor digite S ou N!")
    if cont in "n":
        break
    print("\033[1;31m-\033[m" * 30)

print("\033[1;31m-\033[m" * 30)

print(banco)

#exibir os dados de todos os jogadores
print("""
--------------------------------------------------
| cod  nome            gols             total    |
--------------------------------------------------""")
for i in banco:
    for k,v in i.items():
        if k == "Total":
            print(v, '     |')
        elif k == "cod":
            print('| ',v,end='  ')
        else:
            print(' ', v, ' '*(14 - len(v)), end='')
print("--------------------------------------------------")

#mostrar os dados de um único jogador
while True:
    while True:
        most = int(input("Mostrar os dados de qual jogaodor? (999 para parar) "))
        if most <= num or most == 999:
            break
        print("\033[1;31mXXX\033[m Por favor digite um número válido!")
    if most == 999:
        break
    print(f"  ----- Levantamento de {banco[most]['Nome']} --------")
    for i, v in enumerate(banco[most]["Gols"]):
        print(f"\033[1;33m->\033[m Partida \033[1m{i + 1}\033[m: \033[1;35m{v}\033[m gols")

print(f"\033[1;33m{'=' * 73}\033[m")
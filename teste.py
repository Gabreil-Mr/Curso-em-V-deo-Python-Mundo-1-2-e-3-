a="""print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 93 '}\033[1;33m{'='*30}\033[m")
dados = {}
gols = 0
total = 0

# formando o dicionário
dados["Nome"] = str(input("Nome: ")).title()
partidas = int(input(f"Número de partidas de {dados['Nome']}: "))
dados["Gols"] = []
for i in range(0,partidas):
    dados["Gols"].append(int(input(f"Gols na partida {i+1}: ")))
dados["Total"] = sum(dados["Gols"])

print("\033[1;31m-\033[m"*30)

#exibição básica
print(dados)

print("\033[1;31m-\033[m"*30)

#exibição chave-valor
for k,v in dados.items():
    print(f"\033[1;34m{k}\033[m tem valor \033[m{v}\033[1;35m ")

print("\033[1;31m-\033[m"*30)

#exibição detalhada
print(f"O jogador {dados['Nome']} jogou {partidas} partidas: ")
for i,v in enumerate(dados["Gols"]):
    print(f"\033[1;33m->\033[m Partida \033[1m{i+1}\033[m: \033[1;35m{v}\033[m gols")

print(f"\033[1;33m{'=' * 73}\033[m")

"""
print(a.replace("dados","jog"))

print(f"{'='*30}{' DESAFIO 93 '}{'='*30}")
jog = {}
gols = 0
total = 0

# formando o dicionário
jog["Nome"] = str(input("Nome: ")).title()
partidas = int(input(f"Número de partidas de {jog['Nome']}: "))
jog["Gols"] = []
for i in range(0,partidas):
    jog["Gols"].append(int(input(f"Gols na partida {i+1}: ")))
jog["Total"] = sum(jog["Gols"])

print("-"*30)

#exibição básica
print(jog)

print("-"*30)

#exibição chave-valor
for k,v in jog.items():
    print(f"{k} tem valor {v} ")

print("-"*30)

#exibição detalhada
print(f"O jogador {jog['Nome']} jogou {partidas} partidas: ")
for i,v in enumerate(jog["Gols"]):
    print(f"-> Partida {i+1}: {v} gols")

print(f"{'=' * 73}")



Process finished with exit code 0

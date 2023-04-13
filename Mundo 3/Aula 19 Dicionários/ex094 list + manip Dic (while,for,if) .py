print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 94 '}\033[1;33m{'='*30}\033[m")
usu = {}
banco = []
cont = str
med = 0

#coletar os dados + #colocar eles num dicionario
while cont != "n":
    usu.clear()
    #nome
    usu["nome"] = str(input("Nome: "))
    #sexo
    while True:
        usu["sexo"] = str(input("Sexo:[M/F] ")).lower()
        if usu["sexo"] in "mf":
            break
        print("\033[1;31mXXX\033[m Por favor digite M ou F!")
    #idade
    usu["idade"] = float(input("Idade: "))
    #media
    med += usu["idade"]

#colocar numa lista
    banco.append(usu.copy())

    print("\033[1;35m-\033[m"*10,"Cadastro Efetuado!","\033[1;35m-\033[m"*10)
#perdir para continuar (while)
    while True:
        cont = str(input("Continuar? [S/N] ")).lower()
        if cont in "sn":
            break
        print("\033[1;31mXXX\033[m Por favor digite S ou N!")

    print("\033[1;35m-\033[m"*40)

print(f"\033[1;36m{'-='*9}\033[m Resultados\033[1;36m {'-='*9}\033[m")

#A) contar o número de pessoas cadastradas
print(f"\033[1;34mA)\033[m Pessoas Cadastradas: \033[1;32m{len(banco)}")

#B) calcular a média de idade
med = med/len(banco)
print(f"\033[1;34mB)\033[m Média de idade: \033[1;32m{med:.2f}\033[m")

#C)citar as mulheres
print("\033[1;34mC)\033[m As Mulheres são: \033[1;32m", end='')
for p in banco:
    if p["sexo"] == "f":
        print(p["nome"],end='')
print()

#D) pessoas com idade acima da média
print("\033[1;34mD)\033[m Exibição de dicionário de pessoas com idade acima da média:")
for p in banco:
    if p["idade"] > med:
       for k,v in p.items():
           print(f"\033[1;31m->\033[m \033[1;32m{k}: {v} ",end='')
print()

print(f"\033[1;33m{'=' * 73}\033[m")
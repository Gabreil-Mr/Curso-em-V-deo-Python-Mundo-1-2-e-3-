print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 90 '}\033[1;33m{'='*30}\033[m")
dic = {}

dic['nome'] = str(input("Digite o nome: ")).title()
dic['nota'] = float(input(f"Digite a média de {aluno}: "))
if media > 6:
    dic['situação'] = "aprovado"
else:
    dic['situação'] = "Repetiu de ano!"

print("\033[1;36m-\033[m"*30)

for k,v in dic.items():
    print(f"\033[1;35m->\033[m {k} = {v}")

print(f"\033[1;33m{'=' * 73}\033[m")
print(f"\033[1;33m{'='*30}\033[1;34m{' DESAFIO 91 '}\033[1;33m{'='*30}\033[m")
from datetime import datetime

dados = {}

#coletar os dados
dados["nome"] = str(input("Nome: ")).title()
dados["idade"] = datetime.now().year - int(input("Ano de nascimento: "))
dados["cart"] = int(input("Carteira de Trabalho (0 não tem): "))
if dados["cart"] != 0:
    dados["Ano de contratação"] = int(input("Ano de contratação: "))
    dados["salario"] = int(input("Salário R$: "))
dados["Aposentadoria"] = 45 -(datetime.now().year - dados["Ano de contratação"])

print("\033[1;31m-\033[m"*30)

#exibir
for k,v in dados.items():
    print(f"\033[1;35m-> \033[m\033[1;33m{k}\033[m tem valor \033[1;34m{v}\033[m")


print(f"\033[1;33m{'=' * 73}\033[m")

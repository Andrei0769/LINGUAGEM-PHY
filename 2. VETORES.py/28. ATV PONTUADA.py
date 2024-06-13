import os

# Função sem retorno para exibir o logo do SENAI
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI ===")

# Função para calcular o IMC e retornar a situação
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        situacao = "Abaixo do peso"
    elif 18.5 >= imc < 25:
        situacao = "Peso normal"
    elif 25 >= imc < 30:
        situacao = "Sobrepeso"
    elif 30 >= imc < 35:
        situacao = "Obesidade grau 1"
    elif 35 >= imc < 40:
        situacao = "Obesidade grau 2"
    else:
        situacao = "Obesidade grau 3 (mórbida)"
    return imc, situacao

# Listas vazias para armazenar os dados dos usuários
nomes_completos = []
idades = []
alturas = []
pesos = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break

    sobrenome = input("Digite o sobrenome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes_completos.append(f"{nome} {sobrenome}")
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")

for i in range(len(nomes_completos)):
    imc, situacao = calcular_imc(pesos[i], alturas[i])
    print(f"\nUsuário {i + 1}:")
    print("Nome completo:", nomes_completos[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print("IMC:", round(imc, 2))
    print("Situação:", situacao)

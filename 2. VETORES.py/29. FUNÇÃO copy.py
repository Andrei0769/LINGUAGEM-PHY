import os 

#Função sem retorno 
def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

logoSenai()
nome = input ("Digite o seu Nome: ")

logoSenai()
idade = int(input("Digite a sua idade: "))

logoSenai()
peso = float(input("Digite a seu Peso: "))

logoSenai()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso:.2f}")
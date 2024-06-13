import os 

os.system("cçs || clear")

class Pet:
    def __init__(self, nome, idade, raca, porte, alimentacao):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.porte = porte
        self.alimentacao = alimentacao

# Lista para armazenar os pets
pets = []

# Loop para solicitar os dados de 2 pets
for i in range(2):
    print(f"\nInformações do Pet {i+1}:")
    nome = input("Nome: ")
    idade = input("Idade: ")
    raca = input("Raça: ")
    porte = input("Porte: ")
    alimentacao = input("Alimentação: ")

    # Criando uma instância de Pet com os dados fornecidos e adicionando à lista de pets
    novo_pet = Pet(nome, idade, raca, porte, alimentacao)
    pets.append(novo_pet)

# Imprimir os detalhes dos pets
print("\nDetalhes dos Pets:")
for i, pet in enumerate(pets):
    print(f"\nPet {i+1}:")
    print("Nome:", pet.nome)
    print("Idade:", pet.idade)
    print("Raça:", pet.raca)
    print("Porte:", pet.porte)
    print("Alimentação:", pet.alimentacao)

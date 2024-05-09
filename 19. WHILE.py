import os 

os.system("cls || clear")

nota = float (input("Digite a sua Nota: "))

while (nota < 0 or nota > 10):
    nota = int(input(f"Digite a sua Nota: "))

print(f"Nota: {nota}")
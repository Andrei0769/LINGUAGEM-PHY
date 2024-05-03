import os

# Limpar a tela do console
os.system("cls || clear")

pares = 0
impares = 0

for i in range(1, 6):
    num = int(input(f"Digite o {i}º Número: "))

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Pares: {pares}")
print(f"Ímpares: {impares}")


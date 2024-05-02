import os

os.system("cls || clear")
pares = 0
impares = 0


for i in range(1, 6):
    num = int (input(f"Digite o {i}º Número: "))

    if i %2==0:
        pares += 1
            
    else: 
        impares += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")

            

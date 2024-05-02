import os

os.system("cls || clear")

soma = 0

for i in range(1, 6):
    num = int (input(f"Digite o {i}º Número: "))
    soma += num

print(f"Soma: {soma}")

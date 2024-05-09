import os 

os.system("cls || clear")

media = 0
soma = 0

for i in range (1,5):
    num = float (input(f"Digite a sua {i}º Nota: "))
    soma += num

media = (soma) / 4

print(f"Media: {media}")

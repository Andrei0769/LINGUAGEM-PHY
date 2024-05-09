import os 

os.system("cls || clear")

nota = 0
media = 0
soma = 0

for i in range(1, 4):
    num = float(input(f"Digite o {i}º Nota: "))
    soma += num

    media = (soma) / 3

if media >= 7:
    print("Aprovado") 
elif media < 6.99:
    print("Recuperação")
else: 
    print ("Reprovado")

print(f"Sua média é: {media}")  
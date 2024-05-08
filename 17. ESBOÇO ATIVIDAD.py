import os 

os.system("cls || clear")

nota = 0
media = 0


for i in range(1, 4):
    num = float(input(f"Digite o {i}º Nota: "))


if media >= 7:
    print("Aprovado") 
elif media < 6.99:
    print("Recuperação")
else: 
    print ("Reprovado")

   
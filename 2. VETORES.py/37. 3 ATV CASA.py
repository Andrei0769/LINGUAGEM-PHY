import os 

os.system("cls || clear")
num = []
QtndPares = 0
QtndImpares = 0


for i in range (6):
    numero = int(input(f"Digite o seu {i+1}º Número: "))
    num.append(numero)

    if numero % 2 == 0:
        QtndPares += 1
    else:
     QtndImpares += 1



print(f"Quantidade de números pares: {QtndPares}")
print(f"Quantidade de números ímpares: {QtndImpares}")

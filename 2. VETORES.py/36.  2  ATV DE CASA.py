import os 

os.system("cls || clear")

num = []

for i in range (5):
    num.append(int(input(f"Digite o seu {1+i}º Número: ")))
    

maiornumero = max(num)
menornumero = min(num)



print(f"Seu Maior Número é: {maiornumero}")
print(f"Seu Menor Número é: {menornumero}")
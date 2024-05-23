import os 

os.system("cls || clear")

notas = []
soma = 0 
nota = 0

for i in range (3):
    nota = float (input("Digite a sua Nota: "))
    notas.append(nota)
    soma += nota
media = soma /3 
    
for i in range (3):
        print(f"Nota: {notas[i]}")

print(f"Sua Média é: {media}")




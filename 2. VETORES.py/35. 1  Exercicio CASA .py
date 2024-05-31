import os 

os.system("cls || clear")
notas=[]
media = 0
nota = 0
soma = 0 

for i in range (4):
    nota = float (input(f"Digite a sua {1+i}º Nota: "))
    notas.append(nota)
    

media = sum(notas) / len(notas)

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovaado ")

print(f"Sua Média é: {media}")
print("\nNotas informadas:")
print(f"Nota 1: {notas[0]}")
print(f"Nota 2: {notas[1]}")
print(f"Nota 3: {notas[2]}")
print(f"Nota 3: {notas[3]}")

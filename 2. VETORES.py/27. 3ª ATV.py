import os

os.system("cls || clear ")

QUANTIDADE_NUMEROS= 5

numeros = []
pares = 0
impares = 0

for i in range (QUANTIDADE_NUMEROS):
    num = int (input("Digite seu Numero: "))
    numeros.append(num)
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
for i, num in enumerate (numeros):
    print(f"O {i+1} numero é:  {num}")


print(f"Pares: {pares}")
print(f"Impares: {impares}")
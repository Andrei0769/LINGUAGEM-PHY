import os 

os.system("cls || clear ")

n = 1 
Quantpares = 0
QuantImpares = 0

while n != 0:
    n = int(input("Digite um Valor: ")) 
    if n != 0: 
        if n % 2 == 0:
            Quantpares += 1
        else:
            QuantImpares += 1

print(f"Quantidades de Números Pares: {Quantpares}")
print(f"Quantidades de Números Impares: {QuantImpares}")
import os 

os.system("cls || clear")


# Inicialização das variáveis
numeros = []
pares = 0
soma_pares = 0
impares = 0
soma_impares = 0
positivos = 0
negativos = 0

# Leitura dos números
for i in range(5):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)
    
    if num % 2 == 0:
        pares += 1
        soma_pares += num
    else:
        impares += 1
        soma_impares += num
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

# Cálculos
quantidade_numeros = len(numeros)
maior_numero = max(numeros)
menor_numero = min(numeros)
media_todos = sum(numeros) / quantidade_numeros
media_pares = soma_pares / pares if pares else 0
media_impares = soma_impares / impares if impares else 0

# Resultados
print(f"\nQuantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Quantidade de números positivos: {positivos}")
print(f"Quantidade de números negativos: {negativos}")
print(f"Quantidade total de números inseridos: {quantidade_numeros}")
print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")
print(f"A média de todos os números inseridos é: {media_todos:.2f}")
print(f"A média dos números pares é: {media_pares:.2f}")
print(f"A média dos números ímpares é: {media_impares:.2f}")
print(f"Números lidos na ordem inversa: {list(reversed(numeros))}")
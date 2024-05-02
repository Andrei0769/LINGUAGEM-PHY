import os

os.system("cls || clear")

num1 = int(input("Escreva o 1º Número: "))
num2 = int(input("Escreva o 2º Número: "))

soma = num1 + num2 
multiplicacao = num1 * num2
media = (num1 + num2) / 2

maiornumero = max(num1, num2)
menornumero = min(num1, num2)

if num1 > num2:
    maiornumero = num1
else: 
    maiornumero = num2

if num1 < num2: 
    menornumero = num1
else:
    menornumero = num2


print(f"Soma:{soma}")
print(f"Multiplicação:{multiplicacao}")
print(f"Média: {media}")
print(f"Maior valor:{maiornumero}")
print(f"Menor Valor:{menornumero}")


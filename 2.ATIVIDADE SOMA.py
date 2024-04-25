import os

os.system("cls || clear")

print("==== SOLICITANDO DADOS ====")
numero1 = int(input ("Digite seu 1º Número: "))
numero2 = int(input ("Digite seu 2º Número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2


print(f"1º número: {numero1}")
print(f"2º numero: {numero2}")
print(f"soma: {soma}")
print(f"subtracao: {subtracao}")
print(f"multiplicacao: {multiplicacao}")
print(f"divisao: {divisao}")


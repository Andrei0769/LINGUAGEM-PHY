
import os 
QUANTIDADES_NOTAS = 3
os.system("cls || clear")

resultado = input
a = 0

for i in range (QUANTIDADES_NOTAS):
    a = float (input(f"Digite o seu {1+i}º Nota: "))

operador = input("Digite o seu operador: + - / *: ")

match(operador): 
    case '+': 
        resultado = i + a
    case '-': 
        resultado = i - a
    case '/': 
        resultado = i / a
    case '*': 
        resultado = i * a
    case '_': 
        print("Opção invalida")


print(f"Resultado: {resultado}")
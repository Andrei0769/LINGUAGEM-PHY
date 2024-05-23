import os 
import sys

QUANTIDADES_NUMEROS= 5

numeros = []
maiorNumero = 0
menorNumero =sys.maxsize
os.system("cls || clear ")

for i in range (QUANTIDADES_NUMEROS):
    num = int (input("Digite o seu Numero: "))
    numeros.append(num)
    maiorNumero = max (num, maiorNumero)
    menorNumero = min (num, menorNumero)



print(f"Maior numero: {maiorNumero} ")
print(f"Menor Valor : {menorNumero} ")
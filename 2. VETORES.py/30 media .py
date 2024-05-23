import os 

#Função sem retorno 
QUANTIDADES_NUMEROS = 2
def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def calMedia(soma, QUANTIDADES_NUMEROS):
    return soma / QUANTIDADES_NUMEROS
soma = 0
for i in range (QUANTIDADES_NUMEROS):
    logoSenai()
    num = int(input(f"Digite o seu {i+1} º Numero: "))
    soma += num
media = calMedia(soma, QUANTIDADES_NUMEROS)

logoSenai()
print(f"Media:{media}")
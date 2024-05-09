import os 

# Este comando é para limpar o terminal em sistemas Windows e Unix/Linux
os.system("cls || clear")

media = 0
soma = 0
contador = 0

# Primeira entrada de nota
nota = int(input("Digite uma nota positiva (digite um número negativo para parar): "))

# Verificação para notas positivas e soma
while nota >= 0:
    soma += nota
    contador += 1
    nota = int(input("Digite uma nota positiva (digite um número negativo para parar): "))

# Se o contador for 0, significa que nenhuma nota foi inserida
if contador == 0:
    print("Nenhuma nota foi inserida.")
else:
    media = soma / contador
    print(f"Média aritmética: {media}")

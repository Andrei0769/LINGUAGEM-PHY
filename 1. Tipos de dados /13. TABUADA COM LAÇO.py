import os

os.system("cls || clear")

num = int (input("Digite o Número: "))

print ("=" * 12)
for i in range(1, 11):

    resultado = num * i

    print(num,"x", i, "=", resultado)
print ("=" * 12)

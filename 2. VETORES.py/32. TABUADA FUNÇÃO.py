import os 

#Função sem retorno 
def logoSenai():
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

os.system("cls || clear")

def multiplica(n1,i):
    return n1 * i
logoSenai()
num = int (input("Digite o Número: "))
for i in range (1,11):
    print(f"{num} X {i} = {multiplica(num,i)}")
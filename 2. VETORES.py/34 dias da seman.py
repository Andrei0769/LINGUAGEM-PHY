import os 
os.system("cls || clear")

print("1 Picanha valor R$ 25,00")
print("2 Lasanha valor R$ 20,00")   
print("3 strognoff valor R$ 18,00")
print("4 Bife Acebolado valor R$ 15,00")
print("5 Picanha valor R$ 15,00")
print("6 Pão com ovo valor R$ 5,00")


opcao = int(input("Digite seu Numero: "))
match(opcao): 
    case '1': 
        print("1 Picanha valor R$ 25,00")
    case '2': 
        print("2 Lasanha valor R$ 20,00")  
    case '3': 
        print("3 strognoff valor R$ 18,00")
    case '4': 
        print("4 Bife Acebolado valor R$ 15,00")
    case '5': 
        print("5 Picanha valor R$ 15,00")
    case '6': 
        print("6 Pão com ovo valor R$ 5,00")
import os 

os.system("cls || clear")
mediaAritimetica = 0
nota = 0 
soma = 0

for i in range(2):    
    while True: 
        nota = float(input(f"Digite a sua {i+1} Nota (entre 0 e 10): "))
        if nota < 0 or nota > 10:
            print("Nota invalida. Por favor, tente novamente. \n ")
        else: 
         soma += nota
         break 
    
mediaAritimetica = (soma) / 2

print(f"Media aritimétca: {mediaAritimetica}")
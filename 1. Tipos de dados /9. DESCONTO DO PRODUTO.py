import os

os.system("cls || clear")

nomeProduto = input ("Digite o nome do produto: ")
precoProduto = float (input("Digite o preço do Produto: "))
quantidadeProduto = int (input("Digite a quantidade: "))


if quantidadeProduto <= 5:
        desconto = 0.02
elif quantidadeProduto <= 10:
        desconto = 0.03
else:
        desconto = 0.05
    
totalPagar = precoProduto - (precoProduto * desconto)
    
print("\n==== EXIBINDO RESULTADOS ====")
print("Produto:", nomeProduto)
print("Preço unitário:", precoProduto)
print("Quantidade adquirida:", quantidadeProduto)
print("Total a pagar:",totalPagar)





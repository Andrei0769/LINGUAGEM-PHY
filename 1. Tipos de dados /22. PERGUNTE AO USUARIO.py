import os 

os.system("cls || clear")

notas = []
continuar = True

while continuar:
    print("\n")
    print("Menu:")
    print("S - Inserir mais uma nota")
    print("P - Ver quantas notas foram inseridas")
    print("N - Calcular média aritmética das notas informadas")
    opcao = input("Escolha uma opção: \n").upper()
    print ("\n")
    if opcao == "S":
        nota = float(input("Digite a nota: "))
        notas.append(nota)
    elif opcao == "P":
        print("Foram inseridas", len(notas), "notas.")
    elif opcao == "N":
        if len(notas) == 0:
            print("Nenhuma nota foi inserida.")
        else:
            media = sum(notas) / len(notas)
            print("A média aritmética das notas é:", media)
    else:
        print("Opção inválida.")

    continuar = input("Deseja continuar? (S/N): ").upper() == "S"

print("Programa encerrado.")

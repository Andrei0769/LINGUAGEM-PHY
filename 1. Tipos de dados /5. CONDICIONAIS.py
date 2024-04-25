import os

os.system("cls || clear")

nome = str(input("Digite seu Nome: "))
idade = int(input("Digite sua idade: "))
nota1 = float(input("Digite sua 1º nota: "))
nota2 = float(input("Digite sua 2º nota: "))
nota3 = float(input("Digite sua 3º nota: "))
media = input

media = (nota1+nota2+nota3) / 3

if media >= 7: 
  print("Aprovado") 
else: 
    print("Não Aprovado")

    # === Exibindo Resultados ===
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"1º nota: {nota1}")
print(f"2º nota: {nota2}")
print(f"Média: {media}")
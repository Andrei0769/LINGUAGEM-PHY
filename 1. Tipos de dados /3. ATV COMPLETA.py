import os

os.system("cls || clear")

# Solicitando Dados para o Usúario 
nome = str(input("Digite seu Nome: "))
idade = int(input("Digite sua idade: "))
nota1 = float(input("Digite sua 1º nota: "))
nota2 = float(input("Digite sua 2º nota: "))
nota3 = float(input("Digite sua 3º nota: "))
nota4 = float(input("Digite sua 4º nota: "))
media = input

# Média, soma multiplicação
soma = nota1 + nota2 + nota3 + nota4
multiplicacao = nota1 * nota2 * nota3 * nota4
media = nota1 + nota2 + nota3 + nota4 / 4


print("==== EXIBINDO RESULTADOS ====" )
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"1º nota: {nota1}")
print(f"2º nota: {nota2}")
print(f"3º nota: {nota3}")
print(f"4º nota: {nota4}")
print(f"Soma: {soma}")
print(f"Multiplicação: {multiplicacao}")
print(f"Media: {media}")

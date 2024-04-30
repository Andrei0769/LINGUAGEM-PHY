import os

os.system("cls || clear")

# Solicitando Dados para o Usúario 
nome = str(input("Digite seu Nome: "))
idade = int(input("Digite sua idade: "))

login_coreto = "Dev91164"
senha_correto = "91164"

login = str (input("Digite seu login: "))
senha = str (input("Digite sua Senha: "))

nota1 = float(input("Digite sua 1º nota: "))
nota2 = float(input("Digite sua 2º nota: "))
nota3 = float(input("Digite sua 3º nota: "))
media = input

if login == login_coreto and senha == senha_correto:
    print ("\nAcesso Correto")
else:
    print("Senha ou login incorreto!!")


# Média, soma multiplicação
soma = nota1 + nota2 + nota3
multiplicacao = nota1 * nota2 * nota3
media = (nota1 + nota2 + nota3) / 4

if media >= 5: 
  print("\nAprovado") 
else media <= 4.9:
    print("\nreprovado.")

print("\n==== EXIBINDO RESULTADOS ====" )
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"1º nota: {nota1}")
print(f"2º nota: {nota2}")
print(f"3º nota: {nota3}")
print(f"\nSoma: {soma}")
print(f"Multiplicação: {multiplicacao}")
print(f"Media: {media}")
import os 

#Função sem retorno 
def logoSenai():
    os.system("cls || clear")
    print("=== ===== ===")
    print("=== SENAI ===")
    print("=== ===== ===")

def soma(primeiroNumero, segundoNumero):
    resultado = primeiroNumero + segundoNumero
    return resultado
def multiplicacao(primeiroNumero,  segundoNumero):
    resultado = primeiroNumero / segundoNumero
    return resultado
def divisao(primeiroNumero,  segundoNumero):
    resultado = primeiroNumero / segundoNumero
    return resultado


logoSenai()
nome = input ("Digite o seu Nome: ")
logoSenai()
idade = int(input("Digite a sua idade: "))
logoSenai()
peso = float(input("Digite a seu Peso: "))

logoSenai()
primeiroNumero = int(input("Digite o primeiro Numero: "))
logoSenai()
segundoNumero = int(input("Digite o seu segundo Numero: "))

soma = soma (primeiroNumero, segundoNumero)
multiplicacao = multiplicacao (primeiroNumero, segundoNumero)
divisao = divisao (primeiroNumero, segundoNumero)



logoSenai()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Soma: {soma}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
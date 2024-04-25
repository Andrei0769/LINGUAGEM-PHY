import os

os.system("cls || clear")

def main():
  # vamos pedir para o usuário informar um número
  numero1 = float(input("Informe primeiro Número: "))
  
  # o número é par?
  if numero1 % 2 == 0:
    print("O numero informado é par")
  else:
    print("O numero informado é impar")


if __name__== "__main__":
  main()
import os

os.system("cls || clear")

login_coreto = "Dev91164"
senha_correto = "91164"


login = str (input("Digite seu login: "))
senha = str (input("Digite sua Senha: "))

if login == login_coreto and senha == senha_correto:
    print ("Acesso Correto")
else:
    print("Senha ou login incorreto!!")
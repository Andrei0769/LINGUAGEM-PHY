import os
import math

class SENAI:
    def clear_screen(self):
        # Limpar a tela do console.
        os.system("cls" if os.name == "nt" else "clear")

    def logo(self):
        #Exibir o logo do SENAI.
        self.clear_screen()
        print(" === SENAI ===")

    def calcular_imc(self, peso, altura):
        return peso / math.pow(altura, 2)

    def resultado_imc(self, imc):
        if imc < 18.5:
            return "Muito magro"
        elif imc < 25:
            return "Peso normal"
        elif imc < 30:
            return "Sobrepeso"
        elif imc < 35:
            return "Obesidade grau I"
        elif imc < 40:
            return "Obesidade grau II"
        else:
            return "Obesidade grau III (mórbida)"

    def coletar_dados_usuario(self):
        nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
        
        if nome.lower() == 'sair':
            print("Consulta de IMC Finalizada!!")
            return None

        sobrenome = input("Digite o sobrenome do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        altura = float(input("Digite a altura do usuário (em metros): "))
        peso = float(input("Digite o peso do usuário (em quilogramas): "))
        return (nome, sobrenome, idade, altura, peso)

    def exibir_dados_usuario(self, usuario):
        print("\nDados do usuário: \n")
        print("Nome:", usuario[0])
        print("Sobrenome:", usuario[1])
        print("Idade:", usuario[2])
        print("Altura:", usuario[3], "metros")
        print("Peso:", usuario[4], "quilogramas")
        print()

    def executar(self):
        # Executa o programa.
        usuarios = {}
        while True:
            self.logo()
            dados_usuario = self.coletar_dados_usuario()
            if dados_usuario is None:
                break
            nome, sobrenome, idade, altura, peso = dados_usuario
            imc = self.calcular_imc(peso, altura)
            resultado_imc = self.resultado_imc(imc)
            usuarios[nome] = (nome, sobrenome, idade, altura, peso)
            self.exibir_dados_usuario(usuarios[nome])
            print("IMC:", imc)
            print("Resultado:", resultado_imc)
            continuar = input("Deseja inserir outro usuário? (s/n): ")
            if continuar.lower() != 's':
                print("Consulta de IMC Finalizada, Muito Obrigado")
                break

SENAI().executar()

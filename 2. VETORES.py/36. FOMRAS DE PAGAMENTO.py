import os 
os.system("cls || clear  ")

# Solicitar o valor do produto
valor_produto = float(input("Informe o valor do produto: R$ "))

# Solicitar a forma de pagamento
forma_pagamento = int(input("Informe a forma de pagamento (1- à vista, 2- a prazo): "))

match (forma_pagamento):
    case 1:
        # Pagamento à vista com 10% de desconto
        desconto = valor_produto * 0.10
        total_pagar = valor_produto - desconto
        print("\nDetalhes do pagamento:")
        print(f"Valor do produto: R$ {valor_produto}")
        print("Forma de pagamento: à vista")
        print(f"Valor do desconto: R$ {desconto}")
        print(f"Total a pagar: R$ {total_pagar}")
    
    case 2:
        # Pagamento a prazo
        quantidade_parcelas = int(input("Informe a quantidade de parcelas: "))
        valor_parcela = valor_produto / quantidade_parcelas
        print("\nDetalhes do pagamento:")
        print(f"Valor do produto: R$ {valor_produto}")
        print("Forma de pagamento: a prazo")
        print(f"Quantidade de parcelas: {quantidade_parcelas}")
        print(f"Valor da parcela: R$ {valor_parcela}")
        print(f"Total a prazo: R$ {valor_produto}")
    
    case _:
        print("Opção de pagamento inválida. Tente novamente.")

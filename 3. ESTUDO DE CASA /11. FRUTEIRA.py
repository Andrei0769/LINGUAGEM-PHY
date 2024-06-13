import os

os.system("cls || clear")

pesoMorangos = float (input("Digite o peso do Morango (em Kg): "))
pesoMacas =  float (input("Digite o peso das Maças (em Kg): "))


if pesoMorangos < 5:
    precoMorango = 2.50
else: 
    precoMorango = 2.20

if pesoMacas < 5:
    precoMacas = 2.50
else: 
    precoMacas = 2.20

pesoTotal  = pesoMorangos + pesoMacas
subtotal = (precoMorango * precoMacas) + (precoMacas * pesoMacas)

if pesoTotal > 8 or subtotal > 25:
    desconto =  subtotal * 0.10
else:
    desconto = 0

totalPagar = subtotal - desconto

print ("=== EXIBINDO RESULTADOS ===")

print(f"Peso de Morangos (em Kg): {pesoMorangos}")
print(f"Peso de Maças (em Kg): {pesoMacas}")
print(f"Soma de pesos (em Kg): {pesoTotal}")
print(f"Subtotal: R$ {subtotal}")
print(f"Desconto: R$ {desconto}")
print(f"Total a Pagar: R$ {totalPagar}")
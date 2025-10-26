valor_compra= float(input("Digite o valor da compra:  "))

if valor_compra <= 100:
    desconto= valor_compra* 0.05

elif valor_compra <= 200:
    desconto= valor_compra* 0.10

else:
    desconto= valor_compra* 0.20

valor_final= valor_compra - desconto

print(f"O valor a pagar é {valor_final:.2f} ")

    

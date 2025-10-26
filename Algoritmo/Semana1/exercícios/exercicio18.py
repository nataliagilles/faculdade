idade_eleitor= int(input("Digite a sua idade:  "))

if idade_eleitor== 16 or idade_eleitor== 17:
    print("Eleitor facultativo")

elif 18 <= idade_eleitor <= 65:
     print("Eleitor obrigatório")

elif idade_eleitor > 65:
    print("Eleitor dispensado")

else:
    print("Você não pode votar ainda.")

    

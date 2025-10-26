num= int(input("Digite um número inteiro:  "))

if num < 1:
    print("Por favor digite um número maior que 1")

else:
    hn= 0
    for n in range (1, num + 1):
        hn += 1/ n

    print(f"o numero harmonico {num} é: {hn:.2f}" )
    
    

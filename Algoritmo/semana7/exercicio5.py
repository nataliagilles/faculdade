n= 15
i = 0
lista_elementos=[]
contador_elemento= 0



while contador_elemento < n:
    try:
        elemento = int(input(f"Digite o {contador_elemento + 1}º números inteiro: "))
        lista_elementos.append(elemento)
        contador_elemento += 1

        num_pares= 0
        lista_pares= []
        if elemento %2 == 0:
            num_pares += 1
            lista_pares.append(elemento)

        num_impares= 0
        lista_impares=[]
        else:
            num_impares += 1
            lista_impares.append(elemento)

        soma_pares= sum(lista_pares)
        soma_impares= sum(lista_impares)

    except:
            elemento= int(input("Por favor digite um número inteiro: "))

print(f"Soma dos Pares: {soma_pares}")
print(f"Soma dos ímpares: {soma_impares}")


        
        
        

    

n= int(input("Digite a quantidade de números que serão fornecidos:  "))
i = 0
lista_elementos=[]

while contador_elemento < n:
    try:
        elemento = int(input(f"Digite o {contador_elemento + 1}º números inteiro: "))
        lista_elementos.append(elemento)
     except:
            elemento= int(input("Por favor digite um número inteiro: "))


try:
    num= int(input("Digite um valor (inteiro) para verificar se está presente na lista:  "))

    if num in lista_elementos:
        print(f"O valor {num} está presente na lista.")

    else:
        (f"O valor {num} não está presente na lista.")

except:
    print("Por favor, digite um número inteiro!")
        
        

    

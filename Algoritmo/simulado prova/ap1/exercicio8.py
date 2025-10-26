n= int(input("Digite  a quantidade de valores(inteiro e positivo):  "))
negativo= "-"

    if n <= 0:
        print("Por favor digite um valor inteiro e postivo.")
    if n == negativo:
        print("Por favor digite um valor inteiro e postivo.")

    else:
        contador= 0
        crescente = True
        decrescente = True
        anterior = int(input("Digite o valor 1:  "))

        while contador < n:
          atual= int(input(f"Digite o valor {contador + 1}:  "))

        if atual < anterior:
            crescente = False
        if atual > anterior:
            decrescente = False

        anterior = atual
        contador += 1

        if crecente:
            print(1)
            
        elif decrescente:
            print(-1)

        else:
            print(0)
            

        

        

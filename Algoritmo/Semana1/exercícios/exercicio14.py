A= float(input("Digite o valor de A:  "))
B= float(input("Digite o valor de B:  "))
C= float(input("Digite o valor de C:  "))

if A == 0:
    print("Isso não é uma equação de segundo grau(A não pode ser 0).")

else:
    delta= B **2 - 4 * A * C
    print(f"O valor de delta é {delta}")

    if delta < 0:
        print("A equação não possui raízes reais.")
        
    elif delta == 0:
        raiz= -B / (2*A)
        print(f"A equação possui uma raiz real x= {raiz}")

    else:
        raiz1= (-B + delta ** 0.5)/ (2 * A)
        raiz2= (-B - delta ** 0.5)/ (2 * A)

        print(f"As raízes reais são: \nx1= {raiz1}\nx2= {raiz2}")
        

    



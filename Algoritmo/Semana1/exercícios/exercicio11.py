a= int(input("Digite o valor de A:  "))
b= int(input("Digite o valor de B:  "))

if a > b:
    a,b = b,a

print(f" Em ordem crescente A= {a} e B= {b}")

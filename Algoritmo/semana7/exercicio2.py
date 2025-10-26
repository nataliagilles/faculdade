lista= []
qntd_pessoas= int(input("Digite a quantidade de alturas que serão inseridas:"))
lista_alturas= []

i= 0
while i < qntd_pessoas:
    alturas= float(input(f"Digite a altura da {i + 1}º pessoa: "))
    lista_alturas.append(alturas)
    i += 1
print(lista_alturas)

menor_altura= 1000
for alturas in lista_alturas:
    if alturas < menor_altura:
        menor_altura= alturas
print(f"A menor altura é {menor_altura}")





    

        

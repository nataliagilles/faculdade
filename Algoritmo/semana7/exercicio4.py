lista_geral= []
lista_a= []
lista_b= []
lista_c= lista_a + lista_b

for i in range(10):
    valores= int(input(f"Digite o {i + 1}º valor:"))
    lista_geral.append(valores)


lista_a =lista_geral[0:5]
lista_b =lista_geral[5:10]

lista_c= []
for j in range(len(lista_a)):
    lista_c.append(lista_a[j] + lista_b[j])

print(lista_a)
print(lista_b)
print(lista_c)

    




    

        

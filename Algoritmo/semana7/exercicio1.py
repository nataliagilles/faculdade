lista= []

i= 0
while i < 10:
    num= int(input(f"Digite o {i + 1} valor: "))
    lista.append(num)
    i += 1

print(lista)

if len(lista) >= 10:
    soma= sum(lista)
    print(f"A soma de todos os elemento é: {soma}")

pares= []
for num in lista:
    if  num % 2 == 0:
        pares.append(num)
print(f"Os números pares são: {pares}")
        

        

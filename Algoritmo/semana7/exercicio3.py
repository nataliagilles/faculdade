
lista_temperaturas= []

i= 0
contador= 0
while i < 7:
    temperatura= float(input(f"Digite a {i+1}º temperatura:"))
    lista_temperaturas.append(temperatura)
    i += 1
    
media= sum(lista_temperaturas) / len(lista_temperaturas)

dias_acima_media= 0
for temperatura in lista_temperaturas:
    if temperatura > media:
       dias_acima_media += 1 

        
print(f"A temperatura esteve acima da média {dias_acima_media} dias.")
    






    

        

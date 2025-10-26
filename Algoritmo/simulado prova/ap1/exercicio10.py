frase= input("Digite uma frase:  ")

impares= ''
pares= ''

for i in range(len(frase)):
    if i % 2 == 0:
        impares += frase[i]

    else:
        pares += frase[i]

print(f"Caracteres impares: {impares}")
print(f"Caracteres pares:  {pares}")
print(f"String Final: {impares + pares}")
    
        
    
            

        

        

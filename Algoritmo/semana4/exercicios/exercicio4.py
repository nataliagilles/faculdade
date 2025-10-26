frase= input("Digite uma frase:  ").strip()

i= 0
contador = 0
dentro_palavra= False

while i < len(frase):
    if frase[i] != " " and not dentro_palavra:
        contador += 1
        dentro_palavra= True

    elif frase[i] == " ":
        dentro_palavra= False
    i +=1
print(f"O número de palavras é {contador}")

    
    



text= input("Digite uma string:  ")
text= text.lower()

tem_repeticao= True
for i in range(len(text)):
    ja_apareceu= False

    for j in range(i):
        if text[j]== text[i]:
            ja_apareceu = True

    if not ja_apareceu:
        for k in range( i + 1, len(text)):
            if text[i]== text[k]:
                print(text[i])
                tem_repeticao= True

if not tem_repeticao:
    print("Não há repetiçao de caracteres na string informada")
    
        
    
            

        

        

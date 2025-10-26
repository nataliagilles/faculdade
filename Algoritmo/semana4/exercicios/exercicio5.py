frase= input("Digite uma frase:  ")
letra= input("Digite uma letra:  ")

i= 0
ultima_posicao= -1

while i < len(frase):
    if frase[i] == letra:
        ultima_posicao= i
    i += 1

    if ultima_posicao != -1:
        print(f"A ultima ocorrência da letra {letra} está na posição {ultima_posicao}")
    
        
    

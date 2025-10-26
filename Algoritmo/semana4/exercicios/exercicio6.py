frase= input("Digite uma frase:  ")
letra= input("Digite a letra a ser removida:  ")

i= 0
letra_remover= 0
frase_removida= 0
while i < len(frase):
    if frase[i] == letra:
        letra_remover += 1
        frase_removida += 1


print(f" A o remover a letra {letra} da frase {frase_removida} ")
    
        
        

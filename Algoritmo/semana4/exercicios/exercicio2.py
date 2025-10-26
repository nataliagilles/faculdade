frase= input("Digite uma frase:  ")

contador= 0
for caracter in frase:
    if caracter != " ":
        contador+= 1
        
print(f" A quantidade de caracteres que essa string contém, \ncom exceção de espaços em branco é {contador}")

nome= input("Digite um nome:  ")
invertido_maiusculas= ''

for i in range(len(nome)):
    letra = nome[i]

if letra in maiuscula:
    invertido_maiusculo += maiuscula[letra]

else:
    invertido_maiusculo += letra

print(invertido_maiusculo)
    
    
    

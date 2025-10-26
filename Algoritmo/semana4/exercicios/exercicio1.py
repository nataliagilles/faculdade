palavra= input("Digite algo:  ")

caracter_esquerda= 0
for caracter in palavra:
    caracter_esquerda += 1

caracter_direita= 0
for caracter in range (-1, -(caracter_esquerda + 1), -1):
    caracter_direita += 1

print(caracter_esquerda)
print(caracter_direita)

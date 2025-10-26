num= int(input("Digite um número inteiro:  "))

soma = 0
posicao = 0

while num > 0:
    digito= num %10
    if posicao %2 != 0:
        soma += digito
    num= num //10
    posicao += 1
    
print(f" A soma dos digitos impares da esquerda para direita é: {soma}")
    

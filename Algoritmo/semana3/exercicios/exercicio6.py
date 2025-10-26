num= int(input("Digite um número inteiro:  "))

qntd_pares = 0
qntd_impares = 0
posicao= 0
soma = 0
while num > 0:
    digito= num %10
    num= num //10
    
    if digito %2 == 0:
        qntd_pares += 1  
    else:
        qntd_impares +=1

soma= qntd_pares + qntd_impares

print(qntd_pares)
print(qntd_impares)
print(soma)

    

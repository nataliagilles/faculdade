def divisores(numero):
    lista= []
    for i in range(1, numero + 1):
        if numero % i == 0:
            lista.append(i)
    return lista

n= int(input("Digite um número inteiro:"))

resultado = divisores(n)

print(f"Os divisores de {n} são: {resultado}")
            

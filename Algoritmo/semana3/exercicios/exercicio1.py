
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# Determina o maior e o menor
maior = max(num1, num2)
menor = min(num1, num2)

# Mostra os números do intervalo em ordem decrescente
print("\nNúmeros no intervalo (inclusive), em ordem decrescente:")
for i in range(maior, menor - 1, -1):
    print(i)

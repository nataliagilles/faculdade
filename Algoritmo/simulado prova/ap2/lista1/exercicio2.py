def mdc (a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mdc_lista(lista):
    resultado= lista[0]
    for i in range(1, len(lista)):
        resultado= mdc(resultado, lista[i])
    return resultado


lista_num= []
n= int(input("Digite a quantidade de valores que serão inseridos:"))

for i in range(n):
       num= int(input(f"Digite o {i + 1}º valor:"))
       lista_num.append(num)

print(f"O MDC da lista é: {mdc_lista(lista_num)}")

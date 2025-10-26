n= int(input("Digite a quantidade valores que serão inseridos: "))
lista_num= []

contador= 0
while contador < n:
    contador += 1
    num= int(input(f"Digite o {contador}º valor: "))
    lista_num.append(num)
    
    
encontrar= int(input("Digite um valor a ser encontrado: "))


posicao = 0
achou = False

while posicao < len(lista_num):
    if lista_num[posicao] == encontrar:
        print(f"tem aqui na posição {posicao}")
        achou = True
    posicao += 1

if not achou:
    print("-1")

    

mat=[]
print("Digite nove valores para realocalos em uma matriz 3x3")
for i in range(3):
    linha= []
    for j in range(3):
        valores= int(input(f"Digite o valor para posição [{i}][{j}]:  "))
        linha.append(valores)
    mat.append(linha)

#matriz 3x3
for i in range(3):
    for j in range(3):
        print(mat[i][j], end = " ")
    print()

soma_total= 0
for i in range(3):
    for j in range(3):
        soma_total += mat[i][j]

for i in range(3):
    soma_linha= 0
    for j in range(3):
        soma_linha += mat[i][j]

print(f"Soma total: {soma_total}")
print(f"Soma dos elementos de cada linha: {soma_linha}")

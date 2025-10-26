mat=[]

linhas=int(input("Digite a quantidade de linhas (número inteiro e positivo): "))
colunas= int(input("Digite a quantidade de colunas (número inteiro e positivo): "))

for i in range(linhas):
    linha= []
    for j in range(colunas):
        valor= int(input(f"Digite o valor para posição [{i}][{j}]:  "))
        linha.append(valor)
    mat.append(linha)

for i in range(linhas):
    for j in range(colunas):
        print(mat[i][j], end = " ")
    print()


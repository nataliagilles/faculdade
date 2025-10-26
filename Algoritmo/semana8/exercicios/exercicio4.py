qntd_linha_colunas= int(input("Digite a quantidade de linhas e colunas: "))

if qntd_linha_colunas > 0:
    matriz = []

    print("Digite os elementos da matriz:")
    for i in range(qntd_linha_colunas):
        linha = []
        for j in range(qntd_linha_colunas):
            valor = int(input(f"Elemento [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)

    diagonal = []
    traco = 0

    for i in range(qntd_linha_colunas):
        diagonal.append(matriz[i][i])
        traco += matriz[i][i]

    print("Diagonal principal:", diagonal)
    print("Traço da matriz:", traco)


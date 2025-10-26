#matriz 3 x 4

linhas= 3
colunas= 4
mat= []

for i in range (linhas):        #i= 0,1,2
    mat.append([])
    for j in range(colunas):
        x= int(input(f"Informe o número [(i)] [(j)]: ")
               mat[i].append(x)

    for i in range(linhas):
               for j in range(colunas):
                   print(mat[i][j], end= "")
               print()

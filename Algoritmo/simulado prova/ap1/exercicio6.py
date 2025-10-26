n= int(input("Digite o número de Atletas:  "))
m= int(input("Número de saltos de cada competidor:  "))
melhor_salto_geral = -1
nome_vencedor= ""

contador_atleta =0
while contador_atleta < n:
    nome= input("Digite o nome do atleta:  ")
    melhor_salto_atleta = -1
    
    contador_salto = 0
    while contador_salto < m:
        distancia= float(input(f"Digite a distância saltada{contador_salto + 1}:  "))

        if distancia < 0:
            print("O salto não pode ser negativo.")

        if distancia> melhor_salto_atleta:
            melhor_salto_atleta = distancia

        contador_salto += 1
        
    print(f"O melhor salto de {nome_vencedor} foi {melhor_salto_atleta}")

    contador_atleta += 1
    
    if melhor_salto_atleta > melhor_salto_geral:
        melhor_salto_geral = melhor_salto_atleta
        nome_vencedor = nome

print(f"O vencedor da competição é {nome_vencedor} com um salto de {melhor_salto_geral} metros.")    

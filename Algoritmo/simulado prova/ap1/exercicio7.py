n= int(input("Digite o número de nadadores:  "))
m= int(input("Número de provas que cada competidor realizará:  "))
melhor_tempo_geral = -1
nome_vencedor= ""

contador_nadador = 0
while contador_nadador < n:
    nome= input("Digite o nome do atleta:  ")
    
    contador_tempo = 0
    while contador_tempo < m:
        distancia= float(input(f"Digite o tempo demorado(em segundos){contador_tempo + 1}:  "))
        melhor_tempo_atleta= -1

        if distancia < 0:
            print("O tempo não pode ser negativo.")

        if distancia> melhor_tempo_atleta:
            melhor_tempo_atleta = distancia

        contador_tempo += 1
        
    print(f"O melhor salto de {nome} foi {melhor_tempo_atleta}")

    contador_atleta += 1
    
    if melhor_tempo_atleta > melhor_tempo_geral:
        melhor_tempo_geral = melhor_tempo_atleta
        nome_vencedor = nome

print(f"O vencedor da competição é {nome_vencedor} com um salto de {melhor_tempo_geral} metros.")    

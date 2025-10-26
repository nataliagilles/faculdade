continuar= True
soma_tempo_exercicio= 0
contador= 0
menor_tempo= float('inf')
maior_tempo= -1
nome_menor_temp= ''
qntd_idade_mais50_60min= 0
qntd_idade_25a35_90min= 0
nome_maior_temp= ''


while True:
    nome= input("Digite o nome(para encerrar digite fim):  ")

    if nome == "fim":
        continuar = False
        
    else:
        idade= int(input("Digite a idade:  "))
        tempo_exercicio= float(input("Digite o tempo de exercício:  "))

        soma_tempo_exercicio += tempo_exercicio
        contador += 1

    if tempo_exercicio < menor_tempo:
        menor_tempo = tempo_exercicio
        nome_menor_temp = nome


    if tempo_exercicio %5== 0 and tempo_exercicio > maior_tempo:
         maior_tempo = tempo_exercicio
         nome_maior_temp= nome
        

    if idade > 50 and tempo_exercicio > 60:
        qntd_idade_mais50_60min += 1

    if 25 <=  idade <= 35 and tempo_exercicio > 90:
        qntd_idade_25a35_90min += 1

media= soma_tempo_exercicio / contador
percentual= (qntd_idade_25a35_90min / contador) * 100

print(f"A média de tempo de exercício físico diário de todas as pessoas é: {media:.2f}")
print(f"{menor_tempo:.2f} é o menor tempo registrado de {nome_menor_temp}")
print(f"{maior_tempo:.2f} é o maior tempo registrado de {nome_maior_temp}")
print(f"{qntd_idade_mais50_60min}quantidade de pessoas com idade superior a 50 anos e que realizam mais de 60 min de exercício.")
print(f"{percentual:.2f}O percentual de pessoas com idade entre 25 e 35 anos que realizam mais de 90 min de exercício diário")
        
        
        

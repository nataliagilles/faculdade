idade= int(input("Digite uma idade para iniciar o programa:  "))
soma_tempo= 0
soma_idades= 0
contador= 0
menor_contribuicao= float('inf')
tempo_maior30= 0
salario_maior10mil= 0
idade_40a60anos= 0
maior_salario_20anos_contrib= 0

while idade > 0:
    idade= int(input("Digite a idade (para parar digite qualquer numero negativo):  "))

    if idade > 0:
       tempo_contribuicao= float(input("Digite o tempo de contribuição:  "))
       salario= float(input("Digite o salário:  "))

       soma_tempo += tempo_contribuicao
       soma_idades += idade
       contador += 1

    if  contador > 0:
        media_idades= soma_idades/ contador

    if tempo_contribuicao < menor_contribuicao:
        menor_contribuicao= tempo_contribuicao

    if tempo_contribuicao >= 30:
        tempo_maior30 += 1

    if salario >= 10000:
        salario_maior10mil += 1

    if 40  <= idade <= 60 and tempo_contribuicao > 15:
        idade_40a60anos += 1

    if tempo_contribuicao > 20 and salario > maior_salario_20anos_contrib:
        maior_salario_20anos_contrib = salario

porcentual_trabalhadores= (idade_40a60anos / contador) * 100
        
print(f"{media_idades} é a média de idades dos trabalhadores.")
print(f"{menor_contribuicao} é p menor tempo de contribuição registrado.")
print(f"Existem {tempo_maior30} trabalhadores com mais de 30 anos de contibuição \n e {salario_maior10mil} com um salário superior a 10 mil reias.")
print(f"{porcentual_trabalhadores}% de trabalhadores com idade entre 40 e 60 anoscom mais de 15 anos de contribuição.")
print(f"{maior_salario_20anos_contrib} reais foi o maior salário entre os trabalhadores com mais de 20 anos de contribuiçaõ.")
    

    
        
        
        
        
        
        
        
    

continuar = True
soma_idades = 0
contador = 0
menor_tempo= 0
qntd_mais30_salario_mais10000= 0
idade_40a60_mais15anos_contrib= 0
maior_salario= 0

while True:
    idade= int(input("Digite a idade(para encerrar digite a idade negativa):"))

    if idade < 0:
        continuar= False

    else:
        temp_contribuicao= float(input("Digite o tempo de contribuição:  "))
        salario= float(input("Digite o salário:  "))

        soma_idades += idade
        contador += 1

    if temp_contribuicao < menor_tempo:
        menor_tempo = temp_contribuicao

    if temp_contribuicao > 30 or salario > 10000:
        qntd_mais30_salario_mais10000 += 1

    if 40 <= idade <= 60 and temp_contribuicao > 15:
        idade_40a60_15anos_contrib += 1

    if salario > maior_salario and temp_contribuicao > 20:
        maior_salario = salario

if contador > 0:
    media= soma_idades / contador
    percentual= (idade_40a60_15anos_contribuicao / contador) * 100

    print(f"A média de idade dos trabalhadores é : {media:.2f}")
    print(f"{menor_tempo} é o menor tempo de contribuição registrado")
    print(f"A quantidade de trabalhadores com mais de 30 anos de contribuição ou que recebam um  salário superior a 10 mil é:{qntd_mais30_salario_mais10000}")
    print(f"{percentual}% de trabalhadores com idade entre 40 e 60 anos e que possuem mais de 15 anos de contribuição")
    print(f"O maior salário recebido entre os trabalhadores com mais de 20 anos de contribuição é {maior_salario}")

else:
    print("nenhum trabalhador foi registrado.")



    

    
        

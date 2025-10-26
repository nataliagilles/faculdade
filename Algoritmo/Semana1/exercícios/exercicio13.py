quantidade_livros= int(input("Digite a quantidade de livros escolhidos:  "))

criterioA= 0.25* quantidade_livros + 7.50
criterioB= 0.50* quantidade_livros + 2.50

print(f"A primeira forma de pagamento dará {criterioA} e \na segunda forma de pagamento dará {criterioB}")

if criterioA > criterioB:
    print(f"A segunda forma de pagamento é mais vantajosa")

elif criterioA < criterioB:
    print(f"A primeira forma de pagamento é mais vantajosa")

else:
    print("Ambas formas de pagamento são vantajosas")


escolha_pagamento= input("Digite qual será a forma de pagamento'1' ou '2':  ")

if escolha_pagamento == '1':
    print("Primeira forma de pagamento efetuada com sucesso!")

elif escolha_pagamento == '2':
    print("Segunda forma de pagamento efetuada com sucesso!")

else:
    print("Escolha uma opção válida e tente novamente.")



X= int(input("Digite um número inteiro:  "))
Y= int(input("Digite outro número inteiro:  "))

if X > Y:
        X,Y= Y,X
        
for contador in range(X, Y +1):
    print(contador)

    



total= 0
nota= float(input("Digite a nota do aluno:  "))
primeira_nota= True
while nota >=0:
    if primeira_nota:
        maior= nota
        menor= nota
        maioremenor= nota
        primeira_nota= False

    elif nota >= 6:
        maior= nota
        
    elif nota >= 4 and nota <=6:
        maioremenor= nota

    elif nota <=4:
        menor= nota

        
    total += 1
    nota= float(input("Digite a nota do aluno:  "))
    
if total > 0:
    print(f" Total: {total}")
    print(f" Maior nota ou igual a 6.0:  {maior}")
    print(f" Nota maiores ou iguais a 4.0 e menores que 6.0:  {maioremenor}")
    print(f" Notas menores que 4.0:  {menor}")


    
    

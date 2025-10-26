total= 0
nota= float(input("Digite a nota do aluno:  "))
primeira_nota= True
while nota >= 0:
    if primeira_nota:
        maior= nota
        menor= nota
        primeira_nota= False

    elif nota > maior:
        maior= nota
    elif nota < menor:
        menor= nota
    total += 1
    nota= float(input("Digite a nota do aluno:  "))
    
if total > 0:
    print(f" Total: {total}")
    print(f" Maior nota:  {maior}
    print(f" Manor nota:  {menor}

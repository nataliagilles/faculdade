
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente (≥ 0): "))

# Verifica se expoente é válido
if expoente < 0:
    print("O expoente deve ser maior ou igual a zero.")
else:
    resultado = 1  # qualquer número elevado a 0 é 1

    for i in range(expoente):
        resultado *= base  # multiplica a base por ela mesma

    print(f"{base} elevado a {expoente} é {resultado}")

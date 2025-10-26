s = 0
numerador = 1

for denominador in range (1, 51):
    print(f"{numerador}/{denominador}\n")
    s += numerador/denominador
    numerador += 2

print(f"Soma final: {s}")

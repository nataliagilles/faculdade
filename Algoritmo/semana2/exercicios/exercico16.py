# Valor do salário mínimo
salario_minimo = 1412.00

# Acumuladores gerais
total_folha = 0
total_pecas = 0
maior_salario = 0
operario_maior_salario = 0

# Contadores por classe e sexo
pecas_m_a = pecas_m_b = pecas_m_c = 0
qtd_m_a = qtd_m_b = qtd_m_c = 0

pecas_f_a = pecas_f_b = pecas_f_c = 0
qtd_f_a = qtd_f_b = qtd_f_c = 0

# Início da entrada de dados
while True:
    num = int(input("Número do operário (0 para encerrar): "))
    if num == 0:
        break

    sexo = input("Sexo (M/F): ").strip().upper()
    pecas = int(input("Número de peças fabricadas no mês: "))

    # Determinar classe e calcular salário
    if pecas <= 30:
        classe = 'A'
        salario = salario_minimo
    elif 31 <= pecas <= 35:
        classe = 'B'
        adicional = (pecas - 30) * (0.03 * salario_minimo)
        salario = salario_minimo + adicional
    else:
        classe = 'C'
        adicional = (pecas - 30) * (0.05 * salario_minimo)
        salario = salario_minimo + adicional

    # Mostrar salário do operário
    print(f"Operário {num} - Classe {classe} - Salário: R${salario:.2f}")

    # Atualizar total da folha e total de peças
    total_folha += salario
    total_pecas += pecas

    # Verificar se é o maior salário
    if salario > maior_salario:
        maior_salario = salario
        operario_maior_salario = num

    # Contadores por classe e sexo
    if classe == 'A':
        if sexo == 'M':
            pecas_m_a += pecas
            qtd_m_a += 1
        elif sexo == 'F':
            pecas_f_a += pecas
            qtd_f_a += 1
    elif classe == 'B':
        if sexo == 'M':
            pecas_m_b += pecas
            qtd_m_b += 1
        elif sexo == 'F':
            pecas_f_b += pecas
            qtd_f_b += 1
    elif classe == 'C':
        if sexo == 'M':
            pecas_m_c += pecas
            qtd_m_c += 1
        elif sexo == 'F':
            pecas_f_c += pecas
            qtd_f_c += 1

# Relatório final
print("\n===== RELATÓRIO FINAL =====")
print(f"Total da folha de pagamento: R${total_folha:.2f}")
print(f"Total de peças fabricadas: {total_pecas}")

# Médias de peças por classe e sexo
if qtd_m_a > 0:
    print(f"Média de peças dos homens na Classe A: {pecas_m_a / qtd_m_a:.2f}")
else:
    print("Nenhum homem na Classe A")

if qtd_f_a > 0:
    print(f"Média de peças das mulheres na Classe A: {pecas_f_a / qtd_f_a:.2f}")
else:
    print("Nenhuma mulher na Classe A")

if qtd_m_b > 0:
    print(f"Média de peças dos homens na Classe B: {pecas_m_b / qtd_m_b:.2f}")
else:
    print("Nenhum homem na Classe B")

if qtd_f_b > 0:
    print(f"Média de peças das mulheres na Classe B: {pecas_f_b / qtd_f_b:.2f}")
else:
    print("Nenhuma mulher na Classe B")

if qtd_m_c > 0:
    print(f"Média de peças dos homens na Classe C: {pecas_m_c / qtd_m_c:.2f}")
else:
    print("Nenhum homem na Classe C")

if qtd_f_c > 0:
    print(f"Média de peças das mulheres na Classe C: {pecas_f_c / qtd_f_c:.2f}")
else:
    print("Nenhuma mulher na Classe C")

print(f"Operário com maior salário: {operario_maior_salario} - R${maior_salario:.2f}")
 

maior_temp= float('-inf')
soma_temp= 0
contador = 0
qntd_abaixo_0= 0
temperatura_acima35= 0

n= int(input("Quantas temperaturas serão informadas?:  "))
while contador > n:
    temperatura= float(input("Digite a temperatura(em Celsius):  "))

    if temperatura == "fim":
        print("Calculando...")

    soma_temp += temperatura
    contador += 1
    
    if temperatura > maior_temp:
        maior_temp = temperatura
 
    if temperatura < 0:
        qntd_abaixo_0 += 1

    if temperatura > 35:
        temperatura_acima35 += 1


media= soma_temp / contador
percentual= (temperatura_acima35 * contador) / 100

print(f" A média de temperaturas informadas é {media}")
print(f"{maior_temp}°C é a maior temperatura registrada")
print(f"{qntd_abaixo_0} é a quantidade de temperaturas abaixo de 0°C")
print(f"O percentual de temperaturas acima de 35°C é: {percentual}.")


        
    

def eh_primo(num):
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def primo_na_posicao(posicao):
    if posicao < 1:
        return None  # posição inválida

    contador = 0
    numero = 2

    while True:
        if eh_primo(numero):
            contador += 1
            if contador == posicao:
                return numero
        numero += 1

        
num= int(input("Digite um número:"))

print(primo_na_posicao(num))



        

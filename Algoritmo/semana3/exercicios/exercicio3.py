n = 6
i = 2
j = 3

count = 0
num = 0
resultado = []

while count < n:
    if num % i == 0 or num % j == 0:
        resultado.append(num)
        count += 1
    num += 1

print(' '.join(map(str, resultado)))

def maior_primo(num):
    divisores = 0
    while divisores != 2:
        divisor = num
        divisores = 0
        while  divisor > 0:
            if num % divisor == 0:
                divisores += 1
                divisor -= 1
            else:
                divisor -= 1
        if divisores == 2:
            continue
        num -= 1
    return num


n = int(input("Digite um valor inteiro: "))

print(maior_primo(n))

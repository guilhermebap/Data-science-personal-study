def maximo(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

n1 = int(input("Digite o valor 1:"))
n2 = int(input("Digite o valor 2:"))
n3 = int(input("Digite o valor 3:"))
print(maximo(n1, n2, n3))

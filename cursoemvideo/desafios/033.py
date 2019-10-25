n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 >= n2 and n1 >= n3:
    biggest = n1
elif n2 >= n1 and n2 >= n3:
    biggest = n2
else:
    biggest = n3

if n1 <= n2 and n1 <= n3:
    smallest = n1
elif n2 <= n1 and n2 <= n3:
    smallest = n2
else:
    smallest = n3

print("O menor número informado foi {} e o maior número foi {}".format(smallest, biggest))
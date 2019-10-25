nome = input("Digite seu nome completo: ")
print("-" * 12)

print(nome.upper())
print(nome.lower())
print("O seu nome possui {} letras".format(len("".join(nome.split()))))
print("O seu primeiro nome possui {} letras".format(len(nome.split()[1])))
nome = input("Digite seu nome completo: ").strip()

print("-" * 12)
firstName = nome.split()[0]
lastName = nome.split()[-1]
print("Primeiro nome: {} \nÚltimo nome: {}".format(firstName, lastName))
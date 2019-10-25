salario = float(input("Digite o seu salário: "))

if salario > 1250:
    novoSalario = salario * 1.1
    print("O novo salário será de R${}".format(novoSalario))
else:
    novoSalario = salario * 1.15
    print("O novo salário será de R${}".format(novoSalario))
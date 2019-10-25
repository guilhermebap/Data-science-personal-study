salario = float(input("Digite seu salário: "))
taxa = 15

print("Salário antigo: R${:.2f} \nAumento: {}% \nSalário novo: R${:.2f}".format(salario, taxa, (salario*(taxa/100 + 1))))
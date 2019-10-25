nomeCliente = input("Digite o nome do cliente: ")
dia = input("Digite o dia de vencimento: ")
mes = input("Digite o mês de vencimento: ")
valor = input("Digite o valor da fatura: ")

print("Olá, {}".format(nomeCliente))
print("A sua fatura com vencimento em {} de {} no valor de R$ {} está fechada.".format(dia, mes, valor))

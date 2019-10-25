produto = float(input("Digite o valor do produto: "))

desconto = 5

print("-" * 8)
print("Preço original: R$ {:.2f} \nDesconto: {}%".format(produto, desconto))
print("Novo preço: R${:.2f}".format((produto*(1-5/100))))
print("-"*8)
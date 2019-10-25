from datetime import date
print("O ano atual é {}".format(date.today().year))
ano = int(input("Informe o ano: "))

if (ano % 4 == 0) and not (ano % 100 == 0) or ano % 400 == 0:
    print("O ano {} é bissexto".format(ano))
else:
    print("O ano {} não é bissexto".format(ano))


print("\033[7;30m-=\033[m"*20)
print("\033[7;30m{:^40s}\033[m".format("MÉDIA DE NOTAS"))
print("\033[7;30m-=\033[m"*20)

n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))

media = (n1+n2)/2

print("A média das notas do aluno foi \033[41;30m{:.2f}\033[m".format(media))
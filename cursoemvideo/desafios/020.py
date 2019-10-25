from random import shuffle

aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")
ordem = [aluno1, aluno2, aluno3, aluno4]
shuffle(ordem)

print("A ordem de apresentação será: \n1º - {} \n2º - {} \n3º - {} \n4º - {}".format(ordem[0], ordem[1], ordem[2], ordem[3]))
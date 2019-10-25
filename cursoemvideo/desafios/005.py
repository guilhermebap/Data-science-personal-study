n = int(input("Digite um número inteiro: "))

cores = {"limpa": "\033[m",
         "azul": "\033[4;34m",
         "vermelho": "\033[4;31m"}

print("O número digitado foi {}, seu sucessor é {}{}{} e seu antecessor é: {}{}{}".format(n, cores["azul"], n + 1,
                                                                                          cores["limpa"], cores["vermelho"],n - 1,
                                                                                          cores["limpa"]))
n = int(input("Digite um número: "))

cores = {"limpa": "\033[m",
         "inverte": "\033[7;30m"}

print("{}dobro de {} = {}{}\n"
      "Triplo de {} = {}\n"
      "{}Raiz quadrada de {} = {:.2f}{}"
      .format(cores["inverte"], n, n*2, cores["limpa"], n, n*3,cores["inverte"], n, n**(1/2), cores["limpa"]))
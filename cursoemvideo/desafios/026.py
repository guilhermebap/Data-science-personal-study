frase = input("Digite uma frase qualquer: ").strip()

aNum = frase.lower().count("a")
print("-" * 12)
print("A letra a aparece {} vezes".format(aNum))
print("A letra a aparece pela primeira vez na posição {}".format(frase.lower().find("a")+ 1))
print("A letra a aparece pela última vez na posição {}".format(frase.lower().rfind("a")+1))
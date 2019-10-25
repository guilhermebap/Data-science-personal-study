def vogal(c):
    c = c.lower()
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        return True
    else:
        return False

letra = input("Digite um caractere: ")
print(vogal(letra))

cidade = input("Informe o nome da sua cidade: ").strip()

duvida = "santo" in cidade.split()[0].lower()

if duvida:
    print("Sua cidade começa com a palavra Santo")
else:
    print("A cidade não começa com a palavra Santo")
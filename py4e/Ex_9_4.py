name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
d = dict()
words = list()

for line in handle:
    if not line.startswith("From "): continue
    line.rstrip()
    words = line.split()
    d[words[1]] = d.get(words[1], 0) + 1

bigAddress = None
bigCount = None

#Looking for the most common word
for address, count in d.items():
    if bigAddress is None:
        bigAddress = address
        bigCount = count
    elif count > bigCount:
        bigAddress = address
        bigCount = count
print(bigAddress, bigCount)

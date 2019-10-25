fname = input("Enter file name: ")
if len(fname) < 1: fname = "romeo.txt"
fh = open(fname)
lst = list()
words = list()
for line in fh:
    lst = line.split()
    for word in lst:
        if word not in words:
            words.append(word)
words.sort()
print(words)

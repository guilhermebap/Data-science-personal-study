name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d = dict()

for line in handle:
    if not line.startswith("From "): continue
    line.rstrip()
    words = line.split()
    time = words[5].split(":")
    d[time[0]] = d.get(time[0], 0) + 1

lst = []
for val, key in d.items():
    tup = (val, key)
    lst.append(tup)

lst = sorted(lst) # lst.sort()

for val, key in lst:
    print(val, key)

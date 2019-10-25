import re
txt = open('regex_sum_230994.txt')
numbers = list()
total = 0
for line in txt:
    line.rstrip()
    numbers = re.findall('[0-9]+', line)
    if len(numbers) < 1: continue
    for i in numbers:
        total = total + int(i)
print(total)

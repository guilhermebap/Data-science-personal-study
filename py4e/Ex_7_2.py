# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"
count = 0
total = 0
words = []
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    words = line.split()
    total = total + float(words[1])
average = total/count
print("Average spam confidence: {0:.12f}".format(average))

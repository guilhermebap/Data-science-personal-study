text = "X-DSPAM-Confidence:    0.8475";
l = len(text)
n = text.find(":") + 1
while n < l:
    if text[n].isnumeric():
        break
    else:
        n = n + 1
print(float(text[n:]))

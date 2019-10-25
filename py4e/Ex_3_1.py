hrs = input("Enter Hours: ")
h = float(hrs)
rt = input("Enter rate: ")
rate = float(rt)
if (h <= 40) :
    pay = h * rate
else :
    pay = (40 * rate) + (h - 40) * (rate * 1.5)
print(pay)

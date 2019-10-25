def pay(hour, rate):
    if hours >  40:
        pay = 40 * rate
        pay = pay + (hours - 40) * (rate * 1.5)
    else:
        pay = hours * rate
    return pay

print("Hello user")
hoursSTR = input("Enter how many hours your work this month: ")
try:
    hours = float(hoursSTR)
except Exception as e:
    hours = -1
if hours == -1:
    print("Error, please enter numeric input")
    exit()

rateSTR = input("Enter your rate/hour: ")
try:
    rate = float(rateSTR)
except Exception as e:
    rate = -1
if rate == -1:
    print("Error, please enter numeric input")
    exit()
else:
    print(pay(hours, rate))

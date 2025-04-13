def computepay(hours, rate):
    #print("In computepay")
    if hours > 40:
        reg = rate * hours 
        otp = (hours - 40) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    #print("Returning", pay)
    return pay 
sh = input('Enter hours: ')
sr = input('Enter Rate: ')
fh = float(sh)
fr = float(sr)
#print(fh,fr)
xp= computepay(fh,fr)
print('pay:', xp)
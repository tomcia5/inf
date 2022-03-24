import math
m = float(input("podaj swoją wagę w kg: "))
wz = float(input("Podaj swój wzrost w m: "))

pwz = pow(wz,2)
bmi = m/pwz

if bmi<20:
    print("Masz niedowagę")
elif 20<=bmi<=25:
    print("Masz prawidłową wagę")
elif 25<bmi<=30:
    print("Masz nadwagę")
elif bmi>30:
    print("Otyłość")
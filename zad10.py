import math

a = float(input("Podaj liczbe do sprawdzenia: "))

def czyParzysta(a):
    if a%2==0:
        return True
    else:
        return False
    
wynik=czyParzysta(a)

if wynik==True:
    print(f"Liczba {a} jest parzysta")
else:
 print(f"Liczba {a} jest nieparzysta")
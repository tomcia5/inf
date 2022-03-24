import random

a = random.randint(1, 20)
b = int(input("Zgadnij jaka liczba zostala wylsowana(od 1 do 20): "))
iloscprob = []
iloscprob.append(b)

if b==a and len(iloscprob)==1:
    print(f"BRAWO! Liczba {b} jest liczbą wylosowaną. Odgadłeś za {len(iloscprob)} razem")
else:
    while b!=a:
        b = int(input("ŹLE! Spróbuj jeszcze raz: "))
        iloscprob.append(b)
    else: 
        print(f"BRAWO Liczba {b} jest liczbą wylosowaną. Odgadłeś za {len(iloscprob)} razem")
    


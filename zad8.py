import random
print("podaj zakres liczb, z którego mam wylosować sześć liczb: ")
a=int(input("Podaj liczbę minimalną: "))
b=int(input("podaj liczbę maksymalną: "))
for i in range(6): 
    print(random.randint(a,b))
print("Podaj trzy długości boków do sprawdzenia: ")
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
if a+b<=c:
    print("Nie ma takiego trójkąta!")
elif a+c<=b:
    print("Nie ma takiego trójkąta!")
elif b+c<=a:
    print("Nie ma takiego trójką†a!")
else:
    print("jest taki trójkąt :)")
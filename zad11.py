x = float(input("podaj współrzędną X: "))
y = float(input("Podaj współrzędną Y: "))

if x < 0:
    if y < 0:
        print("Punkt jest w III ćwiartce!")
    elif y > 0:
        print("Punkt jest w II ćwiartce!")
    else:
        print("Punkt lezy na osi współrzędnych!")
elif x > 0:
    if y < 0:
        print("Punkt jest w IV ćwiartce!") 
    elif y > 0:
        print("Punkt jest w I ćwiartce!")
    else:
        print("Punkt lezy na osi współrzędnych!")
else:
    print("Punkt lezy na osi współrzędnych!")
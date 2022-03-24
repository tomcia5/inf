import random
strzaly=[]
losowanie=[]

for i in range(6):
    a=random.randint(1,50)
    losowanie.append(a)
    b=int(input(f"podaj liczbe{i+1} z 6:"))
    while b>50 or b<1:
        print("Podaj liczbe z zakresu od 1 do 50")
        b=int(input(f"Podaj liczbe {i+1} z 6"))
    strzaly.append(b)

print("wylosowane liczby:")
print(*losowanie, sep=', ')
print("twoje liczby:")
print(*strzaly, sep=', ')

trafione=set(losowanie)&set(strzaly)

if len(trafione)>0:
    print(f"trafiles {len(trafione)} z 6 liczb. oto one: {trafione}")
else:
    print("nie trafiles zadnej liczby")
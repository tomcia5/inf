import random
kamień = 1
papier = 2
nozyce = 3

pktkomp=0
pktuzytk=0

while pktkomp != 3 or pktuzytk != 3:
    a=str(input("papier kamien czy nozyce"))
    b=[]
    c = random.randint(1,3)
    b.append(c) 
    if a==1 and b==2:
        pktkomp = pktkomp + 1
    elif a==1 and b==3:
        pktuzytk = pktuzytk + 1
    elif a==1 and b==1:
        pktuzytk = pktuzytk
        pktkomp = pktkomp
    elif a==2 and b==3:
        pktuzytk = pktuzytk + 1
    elif a==2 and b==1:
        pktuzytk = pktuzytk + 1
    elif a==2 and b==2:
        pktuzytk = pktuzytk
        pktkomp = pktkomp

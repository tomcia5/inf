print("Podaj dwie liczby. ")
a=int(input("a: "))
b=int(input("b: "))
print("Dodawanie(a+b): " , a+b)
print("Dodawanie(b+a): " , b+a)
print("odejmowanie(a-b): " , a-b)
print("odejmowanie(b-a): " , b-a)
print("Mnozenie(a*b): " , a*b)
print("Mnozenie(b*a): " , b*a)
if b==0:
    print("Nie mozna wykonać dzielenia przez 0!(a/b)")
else:
    print("Dzielenie(a/b): " , a/b)
if a==0:
    print("nie mozna wykonywac dzielenia przez 0!(b/a)")
else:
    print("Dzielenie(b/a): " , b/a)
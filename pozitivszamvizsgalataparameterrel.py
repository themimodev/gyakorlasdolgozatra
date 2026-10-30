szam=int(input("Írj egy számot: "))

def vizsgal(szam):
    if szam > 0:
        print("Pozitív szám")
    elif szam < 0:
        print("Negatív szám")
    elif szam == 0:
        print("Nulla")

vizsgal(szam)
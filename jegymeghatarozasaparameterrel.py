def jegy(szazalek):

    if szazalek <= 39:
        print("Az eredményed: elégtelen")
    elif szazalek <= 54:
        print("Az eredményed: elégséges")
    elif szazalek <= 69:
        print("Az eredményed: közepes")
    elif szazalek <= 84:
        print("Az eredményed: jó")
    elif szazalek <= 100:
        print("Az eredményed: jeles")
    else:
        print("Hibás százalék!")

pont = int(input("Hány százalékot értél el? "))

jegy(pont)
def belepes():
    felhasznalonev=input("Kérem a felhasználónevet: ")
    jelszo=input("Kérem a jelszót: ")

    if felhasznalonev=="admin" and jelszo=="python":
        print("Sikeres belépés!")
    elif felhasznalonev!="admin":
        print("Ismeretlen felhasználó!")
    else:
        print("Hibás jelszó!")

print("1. Felhasználó próbálkozása")
belepes()

print("\n2. Felhasználó próbálkozása")
belepes()
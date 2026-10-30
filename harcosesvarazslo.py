import random

harcosHp=random.randint(0,9)
varazsloHp=random.randint(0,9)

print(f"JÁTÉK INDUL! Harcos: {harcosHp} HP | Varázsló: {varazsloHp} HP\n")

while harcosHp> 0 and varazsloHp>0:

    harcosLep = random.randint(0, 9)
    varazsloLep = random.randint(0, 9)

    harcosSebzes = random.randint(1, 6)
    varazsloSebzes = random.randint(1, 6)

    if harcosLep==varazsloLep:
        print("Egy mezőre léptetek, harc!!!")
        harcosHp = harcosHp - varazsloSebzes
        if harcosHp<=0:
            print("Harcos meghaltál!")
        else:
            print(f"Harcos túlélted a támadást, maradt még {harcosHp} HP-d!")
        varazsloHp = varazsloHp - harcosSebzes
        if varazsloHp <= 0:
            print("Varázsló meghaltál!")
        else:
            print(f"Varázsló túlélted a támadást maradt még {varazsloHp} HP-d!")
    else:
        print("Nem léptetek egy mezőre!")

print("\nJÁTÉK VÉGE! Valaki (vagy mindenki) elesett a csatában.")






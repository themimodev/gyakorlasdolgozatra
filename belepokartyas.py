eletkor=int(input("Hány éves vagy? "))
belepokartya=input("Van belépő kártyád? ")


if eletkor>=18:
    if belepokartya=="igen":
        print("Beléphetsz!")
    else:
        print("Nincs belépőkártyád.")

print()

eletkor=int(input("Hány éves vagy? "))
belepokartya=input("Van belépő kártyád? ")

if eletkor>=18 and belepokartya=="igen":
    print("Beléphetsz!")
if eletkor <18:
    print("Túl fiatal vagy a belépéshez.")

print()

eletkor=int(input("Hány éves vagy? "))
belepokartya=input("Van belépő kártyád? ")

if eletkor<18:
    print("Túl fiatal vagy.")
elif belepokartya == "igen":
    print("Beléphetsz.")
else:
    print("Nincs belépőkártyád.")


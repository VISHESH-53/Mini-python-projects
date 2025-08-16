import random as rn
x=1
while x==1:
    r=rn.randint(0,5)
    g=int(input("Pick any number fom 0 to 5:-"))
    if g==r:
        print("Winner!")
    else:
        print("Losser!")
    x=int(input("Enter 1 to continue else enter 0:-"))
    

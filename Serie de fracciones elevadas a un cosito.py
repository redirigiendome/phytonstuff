a=int(input("Ingresar numero"))
j=3
ea=4
for i in range(a):
    if i%2==0:
        print("-",end="")
    else:
        print("+",end="")
    print(j,"* z^",j,end="")
    j=j+3
    print(" / ", "y * ",ea)
    ea=ea+3
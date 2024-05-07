n=int(input("Ingresar numero para serie "))

for i in range (n):
    i=i+2
    for v in range (n):
        v=v+2
        if v<i:
            print(i," ",end="")
        else:
            print(v," ",end="")
    print(" ")
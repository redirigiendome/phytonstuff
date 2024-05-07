a=int(input("Ingesar numero"))
j=1
m=1
n=2
l=3
for i in range (a):
    if i%2==0:
        print("+", end="")
    else:
        print("-",end="")
    print("x^",j, " / ", end="")
    j=j+2
    print(m,"*",n, "*",l)
    m=m+1
    n=n+1
    l=l+1
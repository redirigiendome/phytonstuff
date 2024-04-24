a= int(input("ingrese un numero"))
j=1
m=1
g=2
v=3
for i in range (a):
    if i%2 ==0:
        print("+",end="")
    else:
        print("-",end="")
    print(j, " / ",m,"*",g,"*",v)
    m=m+1
    g=g+1
    v=g+1
    j=j+2
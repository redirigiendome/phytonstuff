#Numero de fracciones que se harán
rango=int(input("Ingresar numero "))
Denominador=4
Numerador=3
#for range es lo mismo que "para" de pseint, solamente que no se anota de cuanto en cuanto salta, ni tampoco por donde empieza, Siempre la variable empezara por 1
for i in range (rango):
    if i%2 ==0:
        print("-",end="")
    else:
        print("+",end="")
    print(Numerador,"* z^",Numerador, " / ", "y * ",Denominador)
#Operaciones para que tenga el patron definido
    Denominador=Denominador+3
    Numerador=Numerador+3
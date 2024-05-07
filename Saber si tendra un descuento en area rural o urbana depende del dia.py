e=100
print("Ingrese el numero de dia")
print("[1]Lunes, martes")
print("[2]Miercoles, jueves5")
print("[3]Viernes, sabado o domingo")
dia=int(input("Ingresar numero -> "))
print("En que rango se encuentra")
print("[1] Urbana")
print("[2] Rural")
ar=int(input("Ingresar un numero -> "))
#DIA1
if dia==1:
    if ar==1:
        print("Tiene descuento del 5% ")
        res5=100-5
        print("Usted pagara: ",res5, " bs")
    else:
        if ar==2:
            print("tiene descuento del 10%")
            res10=100-10
            print("Usted pagara: ",res10," bs")
        else:
            print("error")
#DIA2
if dia==2:
    if ar==1:
        print("Tiene descuento del 10% ")
        res10=100-10
        print("Usted pagara: ",res10," bs")
    else:
        if ar==2:
            print("tiene descuento del 20%")
            res20=100-20
            print(" Usted pagara: ",res20, " bs")
        else:
            print("error")
#DIA3
if dia==3:
    if ar==1:
        print("No tiene descuento ")
    else:
        if ar==2:
            print("tiene descuento del 50%")
            res50=100-50
            print("Usted pagara: ",res50," bs")
        else:
            print("error")
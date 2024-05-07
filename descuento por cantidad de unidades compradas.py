
u=100
newer=1
while newer==1:
    a = int(input("Ingresar la cantidad de unidades compradas "))
    
    if a % 2 == 0:
        hu= a*u
        print("El Precio neto es de: ",hu)
        print("La cantidad comprada es par")
        print("Tiene descuento del 10%")
        res1= hu*0.10
        resfin1=hu-res1
        print("La cantidad a pagar sera de: ",resfin1)
    else:
        hu= a*u
        print("El Precio neto es de: ",hu)
        print("La cantidad comprada es impar")
        print("Tiene descuento del 5%")
        res2= hu*0.05
        resfin=hu-res2
        print("La cantidad a pagar sera de: ",resfin)
    print("Desea volver? [1] SI - 2 [No]")
    newer=int(input())
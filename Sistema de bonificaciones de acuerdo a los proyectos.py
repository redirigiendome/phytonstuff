nuev=1
while nuev==1:
    print("Bienvenidos al sistema de bonificaciondes de HANSA Ltda.")
    name=input("Ingrese nombre completo -> ")
    sal=int(input("Ingrese su salario base -> "))
    p=int(input("Cuantos proyectos ha realizado? -> "))
    print(" ")
    print("Nombre del empleado: ", name)
    print("Salario base: ",sal," Bs")
    print("Cantidad de proyectos: ",p)
    total=sal*p
    print("Total acumulado: ", sal, " x ", p, " = ",total)
    if p % 2 ==0:
        bon=total*0.10
        print("Bonificacion de 10 % por numero par de proyectos = ",bon, " Bs")
        totalneto=bon+total
        print("Total ganado :",total, " + ",bon, " = ", totalneto, " Bs")
    else:
        bon2=total*0.05
        print("Bonificacion de 5 % por numero par de proyectos = ",bon2, " Bs")
        totalneto=bon2+total
        print("Total ganado :",total, " + ",bon2, " = ", totalneto, " Bs")
        nuev=int(input("Desea Continuar? [1] Si - [2] No" "->"))
        
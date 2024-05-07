name=input("Ingresar su nombre")
nota1=int(input("Ingresar Primera nota"))
nota2=int(input("Ingresar Segunda nota"))
nota3=int(input("Ingresar Tercera nota"))   
promedio=(nota1+nota2+nota3)/3
print("La nota del estudiante ", name," es de: ",promedio)
if promedio>=51:
    print("El estudiante ",name," Aprobo")
else:
    print("El estudiante ",name," Reprobo")
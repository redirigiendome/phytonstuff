import math
#Gigabyte = 1024 mb

a=int(input("Cuantos GB tiene?  "))

gb=a*1024

#Microdisco = 1.44 mb

microdisco= gb/1.44

print("Espacio total = ",gb )

print("Microdiscos que puede contener = ", microdisco)

print("Redondeado = ",math.ceil (microdisco))
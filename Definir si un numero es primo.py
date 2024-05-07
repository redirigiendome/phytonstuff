
numero = int(input("Introduce un número: "))

def primo(numero): #Definir si es primo
  if numero <= 1:
    return False #false=devuelve la linea 17
  """
  FORMULA PARA HALLAR NUMERO PRIMO
  """
  for i in range(2, numero):
    if numero % i == 0:
      return False
  return True #True= devuelve la linea 15, En otra palabras devuelve que es primo
if primo(numero):
  print(numero, " es un número primo.") #Ponele que es true
else:
  print(numero, " no es un número primo.") #Ponele q es false

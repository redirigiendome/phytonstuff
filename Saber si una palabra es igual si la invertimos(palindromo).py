def es_palindromo(palabra):
#DEF= definir/ definir funcion
  """
  Función que verifica si una palabra es palíndromo.

  Argumentos:
    palabra: La palabra a verificar.

  Devuelve:
    True si la palabra es palindromo, False en caso contrario.
  """
  palabra = palabra.lower().replace(" ", "")  # palabra.lower =Convertir a minúsculas 
                                                                        # replace (x, y) como decir = reemplazar de los x a y
  return palabra == palabra[::-1]  # Invertir la palabra y comparar
#:: = Empieza desde el inicio
#-1 = En orden inverso

palabra = input("Introduce una palabra: ")
#llama a la definicion de la linea 1
if es_palindromo(palabra):
  print("La palabra", palabra, " es un palíndromo.")
else:
  print("La palabra ",palabra, " no es un palíndromo.")
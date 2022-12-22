def rail_fence(text, num_rails):
  # Crea una lista de listas para almacenar los caracteres transpuestos
  transposed = [[] for _ in range(num_rails)]

  # Itera sobre los caracteres de la cadena de entrada
  for i, char in enumerate(text):
    # Añade el carácter a la sublista correspondiente
    if num_rails == 2:
      if i % 2 == 0:
        transposed[0].append(char)
      else:
        transposed[1].append(char)
    elif num_rails == 3:
      if i % 3 == 0:
        transposed[0].append(char)
      elif i % 3 == 1:
        transposed[1].append(char)
      else:
        transposed[2].append(char)

  # Concatena las sublistas de la lista de listas para obtener la cadena cifrada
  return ''.join([''.join(rail) for rail in transposed])

# Prueba de la función
text = 'HELLO WORLD'
ciphertext = rail_fence(text, 2)
print(ciphertext)  
ciphertext = rail_fence(text, 3)
print(ciphertext)  

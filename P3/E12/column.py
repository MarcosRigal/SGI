import random

def columnar_cipher(text, column_length):
  # Divide la cadena de entrada en una matriz de caracteres
  matrix = [text[i:i+column_length] for i in range(0, len(text), column_length)]
  # Rellena la última fila con espacios si es necesario
  matrix[-1] = matrix[-1].ljust(column_length, ' ')

  # Crea una lista con el índice de cada columna en la matriz
  indices = list(range(column_length))
  # Mezcla la lista de índices de forma aleatoria
  random.shuffle(indices)

  # Crea una lista vacía para almacenar los caracteres transpuestos
  transposed = []
  # Itera sobre los índices de la lista mezclada
  for index in indices:
    # Añade los caracteres de la columna correspondiente de la matriz a la lista de caracteres transpuestos
    transposed.extend(row[index] for row in matrix)

  # Concatena la lista de caracteres transpuestos para obtener la cadena cifrada
  return ''.join(transposed)

# Prueba la función
text = 'HELLO WORLD'
ciphertext = columnar_cipher(text, 3)
print(ciphertext)  # Imprime una cadena cifrada diferente cada vez

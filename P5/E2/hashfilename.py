import sys
from Crypto.Hash import MD5

# Obtiene el nombre del fichero de la línea de comandos
file_name = sys.argv[1]

# Abre el fichero en modo de lectura de bytes
with open(file_name, "rb") as f:
    # Crea una instancia del algoritmo MD5
    md5 = MD5.new()

    # Procesa el fichero a través del algoritmo
    md5.update(f.read())

    # Obtiene el hash code como un objeto de bytes
    hash_code_hex = md5.hexdigest()

    # Muestra el hash code
    print(hash_code_hex)
import sys
from Crypto.Hash import MD5

# Obtiene la opción y el nombre del fichero de la línea de comandos
option = sys.argv[1]

if option == "-c":
    
    if len(sys.argv) != 4:
        print('Uso: comparefilehash.py -c entrada.txt entrada.txt')
        sys.exit(1)

    # Obtiene el nombre del segundo fichero de la línea de comandos
    file_name = sys.argv[2]
    file_name_2 = sys.argv[3]

    # Abre los ficheros en modo de lectura de bytes
    with open(file_name, "rb") as f1:
        with open(file_name_2, "rb") as f2:
            # Crea instancias del algoritmo MD5
            md5_1 = MD5.new()
            md5_2 = MD5.new()

            # Procesa los ficheros a través del algoritmo
            md5_1.update(f1.read())
            md5_2.update(f2.read())

            # Obtiene los hash codes como objetos de bytes
            hash_code_1 = md5_1.hexdigest()
            hash_code_2 = md5_2.hexdigest()

            # Compara los hash codes
            if hash_code_1 == hash_code_2:
                print("Los ficheros tienen el mismo hash MD5")
            else:
                print("Los ficheros tienen distinto hash MD5")

elif option == "-h":
    
    if len(sys.argv) != 4:
        print('Uso: comparefilehash.py -h entrada.txt hash')
        sys.exit(1)

    file_name = sys.argv[2]
    # Obtiene el hash MD5 esperado de la línea de comandos
    expected_hash = sys.argv[3]

    # Abre el fichero en modo de lectura de bytes
    with open(file_name, "rb") as f:
        # Crea una instancia del algoritmo MD5
        md5 = MD5.new()

        # Procesa el fichero a través del algoritmo
        md5.update(f.read())

        # Obtiene el hash code como un objeto de bytes
        actual_hash = md5.hexdigest()

        # Compara el hash code obtenido con el hash esperado
        if actual_hash == expected_hash:
            print("El fichero tienen el mismo hash MD5")
        else:
            print("El fichero tienen distinto hash MD5")

else:

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

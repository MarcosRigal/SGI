import sys
import hashlib

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
            # Crea instancias del algoritmo SHA-256
            sha256_1 = hashlib.sha256()
            sha256_2 = hashlib.sha256()

            # Procesa los ficheros a través del algoritmo
            sha256_1.update(f1.read())
            sha256_2.update(f2.read())

            # Obtiene los hash codes como cadenas hexadecimales
            hash_code_1 = sha256_1.hexdigest()
            hash_code_2 = sha256_2.hexdigest()

            # Compara los hash codes
            if hash_code_1 == hash_code_2:
                print("Los ficheros tienen el mismo hash SHA-256")
            else:
                print("Los ficheros tienen distinto hash SHA-256")

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
        sha256 = hashlib.sha256()
        
        # Procesa el fichero a través del algoritmo
        sha256.update(f.read())


        # Obtiene el hash code como un objeto de bytes
        actual_hash = sha256.hexdigest()

        # Compara el hash code obtenido con el hash esperado
        if actual_hash == expected_hash:
            print("El fichero tienen el mismo hash SHA-256")
        else:
            print("El fichero tienen distinto hash SHA-256")

else:

    file_name = sys.argv[1]
    
    # Abre el fichero en modo de lectura de bytes
    with open(file_name, "rb") as f:
        # Crea una instancia del algoritmo MD5
        sha256 = hashlib.sha256()


        # Procesa el fichero a través del algoritmo
        sha256.update(f.read())

        # Obtiene el hash code como un objeto de bytes
        hash_code_hex = sha256.hexdigest()

        # Muestra el hash code
        print(hash_code_hex)
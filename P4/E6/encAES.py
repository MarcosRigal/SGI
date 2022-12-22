import json
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Nombre del fichero de entrada
in_filename = input("Enter the input file name: ")

# Nombre del fichero de salida
out_filename = input("Enter the output file name: ")

# Generar una clave aleatoria de 16 bytes (128 bits)
key = get_random_bytes(16)
print("key = {}".format(key.hex()))

# Inicializar el objeto Cipher con el modo EAX y la clave generada
cipher = AES.new(key, AES.MODE_EAX)

# Leer el contenido del fichero de entrada
with open(in_filename, "rb") as in_file:
    data = in_file.read()

# Encriptar el contenido del fichero
ciphertext, tag = cipher.encrypt_and_digest(data)

# Guardar el nonce, el tag y el texto cifrado en un fichero de salida
with open(out_filename, "wb") as out_file:
    [ out_file.write(x) for x in (cipher.nonce, tag, ciphertext) ]

# Guardar los datos necesarios para desencriptar el fichero en un fichero JSON
result = {}
result["nonce"] = cipher.nonce.hex()
result["tag"] = tag.hex()
result["ciphertext"] = ciphertext.hex()

with open("dataEAX.json", "w") as out_file:
    json.dump(result, out_file)
    

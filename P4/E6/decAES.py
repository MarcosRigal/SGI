import json
from Crypto.Cipher import AES

# Nombre del fichero de salida
out_filename = input("Enter the output file name: ")

# Pedimos al usuario que introduzca la clave en formato hexadecimal
key = input("Enter the key: ")

try:
    key = bytes.fromhex(key) # Convert the key from hexadecimal to bytes

except (ValueError, KeyError):
    print("You entered a non-hexadecimal number")
    exit()


# Abrimos el fichero JSON con la información necesaria para la desencriptación
with open("dataEAX.json") as json_file:
    data = json.load(json_file)

# Obtenemos el nonce, la etiqueta y el texto cifrado del fichero JSON
nonce = data["nonce"]
tag = data["tag"]
ciphertext = data["ciphertext"]

# Convertimos el nonce y la etiqueta a bytes
nonce = bytes.fromhex(nonce)
tag = bytes.fromhex(tag)
ciphertext = bytes.fromhex(ciphertext)

# Inicializamos el objeto cipher con la clave y el nonce
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

# Desencriptamos y verificamos el texto cifrado
plaintext = cipher.decrypt_and_verify(ciphertext, tag)

# Mostramos el texto desencriptado
with open(out_filename, "wb") as out_file:
    out_file.write(plaintext)
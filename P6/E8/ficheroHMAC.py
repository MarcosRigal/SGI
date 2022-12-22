from Crypto.Hash import HMAC, SHA256
# La clave debe ser una cadena de bytes
key = b'key'
# Abrimos el fichero en modo lectura de bytes
with open('entrada.txt', 'r') as f:
    # Leemos todo el contenido del fichero
    message = f.read()
# Creamos un objeto HMAC con la clave y el mensaje
h = HMAC.new(key, message.encode("utf-8"),digestmod=SHA256)
# Calculamos el hash HMAC
hash = h.hexdigest()
print(hash)
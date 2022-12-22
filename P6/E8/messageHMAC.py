from Crypto.Hash import HMAC, SHA256
# La clave debe ser una cadena de bytes
key = b'key'
# El mensaje también debe ser una cadena de bytes
message = b'message'
# Creamos un objeto HMAC con la clave y el mensaje
h = HMAC.new(key, message,digestmod=SHA256)
# Calculamos el hash HMAC
hash = h.hexdigest()
print(hash)
from Crypto.Hash import MD5

# Crea una instancia del algoritmo MD5
md5 = MD5.new()

data = input("Enter the data to encript: ")

# Procesa algunos datos a través del algoritmo
md5.update(data.encode("utf-8"))

# Obtiene el hash code como un objeto de bytes
hash_code_hex = md5.hexdigest()

print(f"Data: {data}")
print(f"Hash: {hash_code_hex}")
print(f"Hash Length: {len(hash_code_hex)}")

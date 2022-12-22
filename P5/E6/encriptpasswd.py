import hashlib
password = "password"
password_hash = hashlib.sha256(password.encode()).hexdigest()
print(password_hash)
from Crypto.Hash import HMAC, SHA256

hmac = HMAC.new(key=b"secretkey", digestmod=SHA256)
hmac.update(b"message")
hash_value = hmac.hexdigest()
print(hash_value)
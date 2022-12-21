import json
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

in_filename = input("Enter the input file name: ")

out_filename = input("Enter the output file name: ")

key = input("Enter the key: ")

try:
    key = bytes.fromhex(key) # Convert the key from hexadecimal to bytes

except (ValueError, KeyError):
    print("You entered a non-hexadecimal number")
    exit()

mode = input("Enter the mode (CBC or CTR): ")

with open(f"data{mode}.json") as json_data:
    b64 = json.load(json_data)

if mode == "CBC":
    iv = b64decode(b64["iv"])
    cipher = AES.new(key, AES.MODE_CBC, iv)

elif mode == "CTR":
    nonce = b64decode(b64['nonce'])
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)

else:
    print("Invalid mode")
    exit()

with open(in_filename, "rb") as in_file:
    ct_bytes = in_file.read()

if mode == "CBC":
    pt_bytes = unpad(cipher.decrypt(ct_bytes), AES.block_size)

elif mode == "CTR":
    pt_bytes = cipher.decrypt(ct_bytes)

with open(out_filename, "wb") as out_file:
    out_file.write(pt_bytes)

print("Decryption completed")
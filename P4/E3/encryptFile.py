import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

#Input file
in_filename = input("Enter the input file name: ")

#Output file
out_filename = input("Enter the output file name: ")

#Read the input file
with open(in_filename, "rb") as in_file:
    data = in_file.read()

#Generate a random key with a size of 16 bytes (128 bits)
key = get_random_bytes(16)
print("key = {}".format(key.hex()))

#Choose the mode (CBC or CTR)
mode = input("Enter the mode (CBC or CTR): ")

result = {}
#Initialize the cipher object
if mode == "CBC":
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    #Encode the initialization vector (IV) in base64
    iv = b64encode(cipher.iv).decode("utf-8")
    result["iv"] = iv
elif mode == "CTR":
    cipher = AES.new(key, AES.MODE_CTR)
    ct_bytes = cipher.encrypt(data)
    nonce = b64encode(cipher.nonce).decode('utf-8')
    result["nonce"] = nonce
else:
    print("Invalid mode")
    exit()


#Encode the ciphertext in base64
ct = b64encode(ct_bytes).decode("utf-8")

#Save the IV and ciphertext in a dictionary
result["ciphertext"] = ct

#Save the dictionary in a JSON file
with open(f"data{mode}.json", "w") as out_file:
    json.dump(result, out_file)

#Save the ciphertext in the output file
with open(out_filename, "wb") as out_file:
    out_file.write(ct_bytes)

print("Encryption completed")
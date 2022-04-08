import requests

BASE_URL = "http://aes.cryptohack.org/block_cipher_starter"

req = requests.get(f"{BASE_URL}/encrypt_flag")
data = req.json()
ciphertext = data["ciphertext"]
print("ciphertext", ciphertext)

req = requests.get(f"{BASE_URL}/decrypt/{ciphertext}")
data = req.json()
plaintext = data["plaintext"]
print("plaintext", plaintext)

print(bytearray.fromhex(plaintext).decode())
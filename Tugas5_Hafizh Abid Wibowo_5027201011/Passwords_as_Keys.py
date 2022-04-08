from Crypto.Cipher import AES

import binascii
import hashlib
import requests
import sys

req = requests.get('https://aes.cryptohack.org/passwords_as_keys/encrypt_flag')
ct_hex = req.json()["ciphertext"]

list = requests.get('https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words')
list = list.text
list = list.split("\n")

for i in list:
    att_key = hashlib.md5(i.encode()).hexdigest()

    ciphertext = bytes.fromhex(ct_hex)
    key = bytes.fromhex(att_key)
    cipher = AES.new(key, AES.MODE_ECB)

    try:
        decrypted = cipher.decrypt(ciphertext)
        r = binascii.unhexlify(decrypted.hex())
        if r.startswith('crypto{'.encode()):
            print("%s" % i)
            print(r.decode('utf-8'))
            sys.exit(0)

    except ValueError as o:
        continue
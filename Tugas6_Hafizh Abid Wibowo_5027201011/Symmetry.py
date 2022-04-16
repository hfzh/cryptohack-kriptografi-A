import requests

url_base = 'http://aes.cryptohack.org/symmetry'

def hack():
  response = requests.get(url="%s/encrypt_flag/" % url_base).json()
  ciphertext = bytes.fromhex(response['ciphertext'])

  iv, ciphertext = ciphertext[:16], ciphertext[16:]

  response = requests.get(url="%s/encrypt/%s/%s" % (url_base, ciphertext.hex(), iv.hex())).json()
  plaintext = bytes.fromhex(response['ciphertext'])
  return plaintext.decode()

if __name__ == '__main__':
  flag = hack()
  print(flag)
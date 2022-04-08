import requests

url_base = 'http://aes.cryptohack.org/ecbcbcwtf'

BLOCK_SIZE = 16

def hack():
  response = requests.get(url="%s/encrypt_flag/" % url_base).json()
  ciphertext = response['ciphertext']
  
  response = requests.get(url="%s/decrypt/%s" % (url_base, ciphertext)).json()
  plaintext = bytes.fromhex(response['plaintext'])
  ciphertext = bytes.fromhex(ciphertext)

  flag = bytearray()
  for i in range((len(ciphertext)//BLOCK_SIZE)-1):
    flag.extend(bytearray(a ^ b for a, b in zip(ciphertext[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE], plaintext[(i+1)*BLOCK_SIZE:(i+2)*BLOCK_SIZE])))
  return flag.decode()

if __name__ == '__main__':
  flag = hack()
  print(flag)
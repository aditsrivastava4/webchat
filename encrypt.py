from Crypto.PublicKey import RSA
from Crypto import Random

query = input()

random_generator = Random.new().read
key = RSA.generate(2048, random_generator)

fkey = key.exportKey('PEM', passphrase='af9a936b')

pub_key = key.publickey()
f = open('RSA_Key.adit','wb')
f.write(fkey)
f.close()

enc_data = pub_key.encrypt(query.encode(), 32)[0]

f = open('data.adit','wb')
f.write(enc_data)
f.close()
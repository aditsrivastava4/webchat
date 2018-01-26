from Crypto.PublicKey import RSA

def getOrigin():
	"""
	It will decrypt the original key and return it
	"""
	f = open('RSA_Key.adit')
	d = f.read()
	f.close()

	key = RSA.importKey(d,passphrase='af9a936b')
	pub = key.publickey()

	f = open('data.adit','rb')
	ed = f.read()
	f.close()

	de_data = key.decrypt(ed)
	return de_data.decode()

def confirm(passphrase):
	"""
	It will check if the original key and the user entered key match
	"""
	if passphrase==getOrigin():
		return True
	return False
from phe import paillier

def send(user, x, public_key):
	print(x)
	return public_key.encrypt(x)
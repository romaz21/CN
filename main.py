from client_side import send
from server_side import receive
import math
from phe import paillier
import rsa

public_key, private_key = rsa.newkeys(64)

print(public_key)
secret_number_list = [3, 2]
users = ["Roma", "Vova"]
host = "DESKTOP-B4KL41Q"
port = 12345
print(rsa.core.encrypt_int(2, public_key.e, public_key.n))
a = {name: int(send(name, x, public_key, host, port)) for name, x in zip(users, secret_number_list)}
print(a)
print(rsa.core.decrypt_int(a['Vova'], private_key.d, public_key.n))
print(math.isclose(rsa.core.decrypt_int(a['Vova'], private_key.d, public_key.n), math.prod(secret_number_list)))
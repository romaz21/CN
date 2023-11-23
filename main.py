from client_side import send
from server_side import receive
import math
from phe import paillier

public_key, private_key = paillier.generate_paillier_keypair()

secret_number_list = [3.141592653, 300, -4.6e-12]
users = ["Roma", "Vova", "Matvey"]

a = {name: send(name, x, public_key) for name, x in zip(users, secret_number_list)}
print(math.isclose(private_key.decrypt(receive(a)), sum(secret_number_list)))
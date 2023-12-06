import rsa
import socket
import math

def send(user, x, public_key, host, port):
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = "DESKTOP-B4KL41Q"
	port = 12345
	client_socket.connect((host, port))
	print(rsa.core.encrypt_int(x, public_key.e, public_key.n))
	message = str(rsa.core.encrypt_int(x, public_key.e, public_key.n))
	client_socket.send(message.encode())
	response = client_socket.recv(1024)
	print(f"Ответ от сервера: {response.decode()}")
	client_socket.close()
	return response.decode()
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "DESKTOP-B4KL41Q"
port = 12345
client_socket.connect((host, port))
message = "1"
client_socket.send(message.encode())
response = client_socket.recv(1024)
print(f"Ответ от сервера: {response.decode()}")
client_socket.close()
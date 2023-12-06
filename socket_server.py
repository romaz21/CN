import socket
import math 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
print(host)
port = 12345
server_socket.bind((host, port))
server_socket.listen(5)
values = []
while True:
    client_socket, addr = server_socket.accept()
    print(f"Подключение от {addr}")
    data = client_socket.recv(1024)
    print(f"Получены данные: {data.decode()}")
    values.append(int(data.decode()))
    client_socket.send(str(math.prod(values)).encode())
    client_socket.close()
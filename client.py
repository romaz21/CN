import socket
import sys
import time
 
# Создаем TCP/IP сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Подключаем сокет к порту, через который прослушивается сервер
server_address = ("192.168.56.1", 10000)
sock.connect(server_address)
print("Подключено к {} порт {}\n".format(*server_address))
 
while True:
    try:
        # Отправка данных
        mess = input("Введите данные: ")
        print(f"Отправка: {mess}")
        message = mess.encode()
        sock.sendall(message)
        print("Данные отправлены!")
        # Смторим ответ
        amount_recieved = 0
        amount_expected = len(message)
        while amount_recieved < amount_expected:
            data = sock.recv(16)
            amount_recieved += len(data)
            mess = data.decode()
            print(f"Получено: {mess}\n")
    except:
        print("Закрываю сокет...")
        sock.close()
        print("Сокет закрыт.")
        break
time.sleep(5)